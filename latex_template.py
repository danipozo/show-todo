template_head = """
\\documentclass[11pt]{{article}}

\\usepackage[spanish]{{babel}}
\\usepackage[utf8]{{inputenc}}
\\usepackage[dvipsnames]{{xcolor}}

\\title{{\\textbf{{{0}}} }}
\\author{{}}
\\date{{\\today}}
\\begin{{document}}

\\maketitle

\\begin{{center}}
	\\begin{{tabular}}{{c|l}}
	Localización & Nota\\\\ \\hline
"""

template_tail = """
\\end{tabular}
\\end{center}

\\end{document}
"""
