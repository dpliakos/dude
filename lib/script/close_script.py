from .executable import ExecutableScript

class CloseScript(ExecutableScript):

    def __init__(self, name):
        super().__init__(name, './scripts/close-scripts','/tmp/dude/close-scripts')
        
