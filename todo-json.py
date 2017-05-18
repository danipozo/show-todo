import os, glob, argparse, sys, re, fnmatch, json
import Config

# Build argument parser
# parser = argparse.ArgumentParser(description='Show FIXMEs, TODOs or whatever present in a project')
# parser.add_argument('-f', '--file', type=str, default='.rules', help='Specify rule file. .rules by default.')


# Parse arguments and decide which color format to apply
# args = vars(parser.parse_args())


conf = Config.ShowTodoConfig()
# List files matching the regular expressions in the file specified with -f
# files = []
# lines = []
# with open(args['file'], 'r') as rules_f:
#     for line in rules_f:
#         lines.append(line.rstrip('\n')) # TEST THIS

files = []
for dp, dn, filenames in os.walk('.'):
    for ff in filenames:
        for line in conf.filePatterns:
            if fnmatch.fnmatch(ff, line):
                files.append(os.path.join(dp, ff))


# Do the actual matching
output = []
exprs = [re.compile(expr) for expr in conf.matchPatterns]
for f in files:
    with open(f, 'r') as file:

        i = 1
        for line in file:
            match = False

            positions = []
            matchesDicts = []
            j = 1
            for p in exprs:
                ms = p.finditer(line)

                for m in ms:
                    match = True
                    matchesDicts.append({ "exprNum" : j, "positions" : { "first" : m.start(), "last" : m.end() } })
                    # line = insert_color_mark(c, conf.colors.END_DELIMITER, line, m.start(), m.end())

                j = j+1
                    
            if match == True:
                output.append({"lineNum" : i,
                               "text" : line, "matches" : matchesDicts,
                               "file" : f })

                # if args['output_format'] == 'latex':
                #     line = line.replace('%', '\%')
                #     line = line.replace('_', '')
                #     line = line.replace('#', '\#')
                #     line = line.replace('@', '\@')
                # print(line_format_string.format(f,i,line.rstrip()))
            i = i+1

json.dump(output, sys.stdout)
