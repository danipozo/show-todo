# Configuration file.

class ShowTodoConfig:

    def __init__(self):
        self.filePatterns = [
                '*.cpp'
        ]

        self.matchPatterns = [
                'FIXME',
                'TODO',
                'WARNING'
        ]
