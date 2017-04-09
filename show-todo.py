import os, glob, argparse, sys

# files = [f for f in glob.glob('./*') if os.path.isfile(f)]

config_file = ".rules"

def change_config_file(s):
    config_file = s

parser = argparse.ArgumentParser(description='Show FIXMEs, TODOs or whatever present in a project')
parser.add_argument('-f', '--file', type=str, help='Specify rule file. .rules by default.')

args = vars(parser.parse_args())

# if 'file' in args:
#     print(vars(args)['file'])
