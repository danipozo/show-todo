import os, glob, argparse, sys, re, fnmatch, json
import Config

parser = argparse.ArgumentParser(description='Find TODOs, FIXMEs, etc. (or arbitrary patterns) in a code file.')
parser.add_argument('directory')

args = vars(parser.parse_args())
conf = Config.ShowTodoConfig()

files = []
for dp, dn, filenames in os.walk(args['directory']):
    for ff in filenames:
        for line in conf.filePatterns:
            if fnmatch.fnmatch(ff, line):
                files.append(os.path.join(dp, ff))


# Do the actual matching
output = [{ "exprs" : [expr for expr in conf.matchPatterns] }]
exprs = [re.compile(expr) for expr in conf.matchPatterns]
for f in files:
    with open(f, 'r') as file:

        i = 1
        for line in file:
            match = False

            positions = []
            matchesDicts = []
            j = 0
            for p in exprs:
                ms = p.finditer(line)

                for m in ms:
                    match = True
                    matchesDicts.append({ "exprNum" : j, "positions" : { "first" : m.start(), "last" : m.end() } })

                j = j+1
                    
            if match == True:
                output.append({"lineNum" : i,
                               "text" : line, "matches" : matchesDicts,
                               "file" : f })

            i = i+1

json.dump(output, sys.stdout)
