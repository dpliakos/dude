from .scipt import Script
from ..utils.file import File
from ..utils.directory import Directory

class GitHook(Script):

    def __init__(self, gitpath, type, template):
        self.basepath = './scripts/githooks'
        self.gitDir = Directory(gitpath)
        self.type = type
        self.template = template
        path = '{}/{}'.format(self.basepath, template)
        self.path = path
        self.originalFile = File(path)
        self.file = self.originalFile.createTempCopy()

    def place(self):
        target = '{}/{}'.format(self.basepath, self.template)
        final = File(target)
        final.makeExecutable()
