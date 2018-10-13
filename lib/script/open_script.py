from .executable import ExecutableScript


class OpenScript(ExecutableScript):

    def __init__(self, name):
        super().__init__(name, './scripts/open-scripts', '/tmp/dude/open-scripts')

        
