import os, glob, argparse, sys, subprocess, re
import config

conf = config.ShowTodoConfig()

def insert (source_str, insert_str, pos):
    return source_str[:pos]+insert_str+source_str[pos:]

parser = argparse.ArgumentParser(description='Show FIXMEs, TODOs or whatever present in a project')
parser.add_argument('-f', '--file', type=str, default='.rules', help='Specify rule file. .rules by default.')


args = vars(parser.parse_args())

files = []
with open(args['file'], 'r') as rules_f:
    for line in rules_f:
        files += [f for f in glob.glob('./'+line.strip()) if os.path.isfile(f)]

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
                    line = insert(line,c,m.start())
                    line = insert(line,'\033[0m', m.end()+5)

            if match == True:
                print("{0}:{1} {2}".format(f,i,line.rstrip()))

            i = i+1
