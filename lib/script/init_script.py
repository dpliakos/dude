from .executable import ExecutableScript

class InitScript(ExecutableScript):

    def __init__(self, name):
        super().__init__(name, './scripts/init-scripts', '/tmp/dude/init-scripts')
        
