from .executable import ExecutableScript

class CleanScript(ExecutableScript):

    def __init__(self, name):
        super().__init__(name, './scripts/clean-scripts', '/tmp/dude/clean-scripts')
        
