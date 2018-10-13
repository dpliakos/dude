from datetime import datetime
from ..utils.file import File
from .script import Script

class ExecutableScript(Script):
    def __init__(self, name, basepath, basetarget):
        super().__init__(name, basepath, basetarget)
        
    def execute(self):
        self.tmpFile.makeExecutable()
        self.tmpFile.execute()
