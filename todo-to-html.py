import sys, argparse, json
import jinja2
import TodoToHTMLConfig


parser = argparse.ArgumentParser(description='Export output from show-todo to an HTML page')
parser.add_argument('-t', '--template', type=str, default='template.html',
                    help='Specify template file. Default: template.html.')

parser.add_argument('-o', '--output', type=str, default='todo.html',
                    help='Specify output file. Default: todo.html.')

parser.add_argument('--title', type=str, default='TODOs',
                    help='Specify output document title. Default: TODOs.')

args = vars(parser.parse_args())
conf = TodoToHTMLConfig.Config()

# Pipe todo-json.py output
prog_input = sys.stdin.read()

template = jinja2.Template(open(args['template'], 'r').read())

data = json.loads(prog_input)
exprs = data.pop(0)['exprs']

items = []

for d in data:
    # Color title
    item = { "patterns" : [ (exprs[m['exprNum']], conf.colors[m['exprNum']]) for m in d['matches'] ] }

    # Copy rest of data
    item['text'] = d['text']
    item['lineNum'] = d['lineNum']
    item['file'] = d['file']
    
    items.append(item)

with open(args['output'], 'w') as f:
    f.write(template.render(items=items, title=args['title']))
