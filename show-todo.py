import os, glob, argparse, sys, subprocess, re, fnmatch
import config


def insert (source_str, insert_str, pos):
    return source_str[:pos]+insert_str+source_str[pos:]

# Insert two delimiters around a substring in the given string s.
def insert_color_mark(delimiter_start, delimiter_end, s, pos_start, pos_end):
    s = insert(s, delimiter_start, pos_start)
    s = insert(s, delimiter_end, pos_end+len(delimiter_start))

    return s

# Build argument parser
parser = argparse.ArgumentParser(description='Show FIXMEs, TODOs or whatever present in a project')
parser.add_argument('-f', '--file', type=str, default='.rules', help='Specify rule file. .rules by default.')
parser.add_argument('--output-format', type=str, default='term', choices=['term', 'latex'])

# Parse arguments and decide which color format to apply
args = vars(parser.parse_args())
colors = config.TermColors

if args['output_format'] == 'latex':
    colors = config.LatexColors

conf = config.ShowTodoConfig(colors)

# List files matching the regular expressions in the file specified with -f
files = []
for dp, dn, filenames in os.walk('.'):
    for ff in filenames:
        files.append(os.path.join(dp, ff))

with open(args['file'], 'r') as rules_f:
    for line in rules_f:
        files += fnmatch.filter(files, line)


# for dp, dn, filenames in os.walk(path):
#     for ff in filenames:
#         if fnmatch.fnmatch(ff, 'My patterns here'):
#              list.append(os.path.join(dp, ff))
        
exprs = [(re.compile(expr), conf.expressions[expr]) for expr in conf.expressions]
for f in files:
    with open(f, 'r') as file:
        
        i=1
        for line in file:
            match = False
            for p,c in exprs:
                ms = p.finditer(line)

                for m in ms:
                    match = True
                    # line = insert(line,c,m.start())
                    # line = insert(line,'\033[0m', m.end()+5)
                    line = insert_color_mark(c, conf.colors.END_DELIMITER, line, m.start(), m.end())
                    
            if match == True:
                print("{0}:{1} {2}".format(f,i,line.rstrip()))

            i = i+1
