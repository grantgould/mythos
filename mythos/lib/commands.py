class Command:
    """Base Command"""

    def __init__(self, application):
        self.application = application

    def run(self):
        raise NotImplementedError("Subclass must implement abstract method")

class AliasCommand(Command):
    pass

class Quit(Command):
    """quit the application"""

    name = "quit"

    def run(self, _):
        self.application.quit()

class Exit(Quit, AliasCommand):
    """alias for quit"""

    name = "exit"

class QuitShortCut(Quit, AliasCommand):
    """alias for quit"""

    name = "q"

class ExitShortCut(Exit, AliasCommand):
    """alias for quit"""
    
    name = "e"