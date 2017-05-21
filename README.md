# show-todo
Shows TODOs, FIXMEs, etc. in a project.

![Screenshot](screenshot.png)

## How it works
When run in a directory, `todo-json.py` will scan all files in subdirectories matching
some regular expressions specified in the configuration file (`Config.py`) for the
expressions of interest (by default `FIXME`, `TODO` and `WARNING`). It will then output
a piece of JSON to be treated by other programs.

`todo-to-html.py` takes this output and processes it producing an HTML web page using a
[Jinja2](https://jinja.pocoo.org) template. Default template uses [Bulma](https://bulma.io) and [MathJax](https://mathjax.org).

`show-todo.py` is deprecated code.

## Usage
You can use only `todo-json.py` and write your own code to process its output. To use
`todo-to-html.py` with the default template, you'll need to tweak it to point to
Bulma and MathJax sources (I use them locally installed).

## Configuration
Configuration is done by editing each script's configuration file (`Config.py` and `TodoToHTMLConfig.py`) as needed. Their contents are quite self-descriptive.