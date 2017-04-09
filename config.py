class ShowTodoConfig:
    # Colors. Add more as needed.
    RED = "\033[91m"
    YELLOW = "\033[93m"
    PURPLE = "\033[95m"

    # Regular expressions along with colors.
    expressions = {
    "FIXME": RED,
    "WARNING": YELLOW,
    "TODO": PURPLE
    }
