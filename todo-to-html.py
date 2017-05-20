import sys, argparse, json
import jinja2


parser = argparse.ArgumentParser(description='Export output from show-todo to an HTML page')
parser.add_argument('-t', '--template', type=str, default='template.html',
                    help='Specify template file. Default: template.html.')

parser.add_argument('-o', '--output', type=str, default='todo.html',
                    help='Specify output file. Default: todo.html.')

parser.add_argument('--title', type=str, default='TODOs',
                    help='Specify output document title. Default: TODOs.')

# Get program arguments
args = vars(parser.parse_args())

# Pipe todo-json.py output
prog_input = sys.stdin.read()

template = jinja2.Template(open(args['template'], 'r').read())

data = json.loads(prog_input)
exprs = data.pop(0)['exprs']

items = []

for d in data:
    item = { "pattern" : ', '.join([ exprs[m['exprNum']] for m in d['matches'] ]) }
    item['text'] = d['text']
    
    items.append(item)

with open(args['output'], 'w') as f:
    f.write(template.render(items=items, title=args['title']))
