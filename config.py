# Colors. Add more as needed.
class TermColors:
    RED = "\033[91m"
    YELLOW = "\033[93m"
    PURPLE = "\033[95m"

    END_DELIMITER = "\033[0m"

class LatexColors:
    RED = "\\textcolor{red}{"
    YELLOW = "\\textcolor{yellow}{"
    PURPLE = "\\textcolor{purple}{"

    END_DELIMITER = "}"
    

class ShowTodoConfig:

    def __init__(self, colors):
        self.colors = colors
        # Regular expressions along with colors.
        self.expressions = {
        "FIXME": self.colors.RED,
        "WARNING": self.colors.YELLOW,
        "TODO": self.colors.PURPLE
        }
