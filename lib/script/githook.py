from .scipt import Script
from ..utils.file import File
from ..utils.directory import Directory

class GitHook(Script):

    def __init__(self, gitpath, type, template):
        self.gitDir = Directory(gitpath)
        self.type = type
        self.template = template
        path = 'scripts/githooks/{}'.format(template)
        self.originalFile = File(path)
        self.file = self.originalFile.createTempCopy()

    def place(self):
        pass
