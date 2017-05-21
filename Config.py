# Configuration file.

class ShowTodoConfig:

    def __init__(self):
        self.filePatterns = [
                '*.tex',
                '*.md',
                '*.py'
        ]

        self.matchPatterns = [
                'FIXME',
                'TODO',
                'WARNING'
        ]
