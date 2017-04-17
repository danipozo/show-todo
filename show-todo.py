import os, glob, argparse, sys, subprocess, re, fnmatch
import config, latex_template


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
parser.add_argument('--output-format', type=str, default='term', choices=['term', 'latex'], help="Specify output format. Must be one of: term (default), latex")
parser.add_argument('-t', '--title', type=str, default='Notes', help='When using output format latex, specify the title of the resulting document')


# Parse arguments and decide which color format to apply
args = vars(parser.parse_args())
colors = config.TermColors
template = ""
line_format_string = "{0}:{1} {2}"

if args['output_format'] == 'latex':
    colors = config.LatexColors
    template = latex_template.template_head.format(args['title'])
    line_format_string = "\\verb+{0}:{1}+ & {2}\\\\"
    print(template)

conf = config.ShowTodoConfig(colors)

# List files matching the regular expressions in the file specified with -f
files = []
lines = []
with open(args['file'], 'r') as rules_f:
    for line in rules_f:
        lines.append(line.strip())
    
for dp, dn, filenames in os.walk('.'):
    for ff in filenames:
        for line in lines:
            if fnmatch.fnmatch(ff, line):
                files.append(os.path.join(dp, ff))

# with open(args['file'], 'r') as rules_f:
#     for line in rules_f:
#         files += fnmatch.filter(files_tmp, line)

        
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
                    line = insert_color_mark(c, conf.colors.END_DELIMITER, line, m.start(), m.end())
                    
            if match == True:
                line = line.rstrip()

                if args['output_format'] == 'latex':
                    line = line.replace('%', '\%')
                    line = line.replace('_', '')
                    line = line.replace('#', '\#')
                    line = line.replace('@', '\@')
                print(line_format_string.format(f,i,line.rstrip()))

            i = i+1

if args['output_format'] == 'latex':
    print(latex_template.template_tail)
