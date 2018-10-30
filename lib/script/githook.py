from .scipt import Script
from ..utils.file import File
from ..utils.directory import Directory

class GitHook(Script):

    # REVIEW: check comments at the script.py
    def __init__(self, gitpath, type, template):
        self.basepath = './scripts/githooks'
        self.gitDir = Directory(gitpath)
        self.type = type
        self.template = template
        path = '{}/{}'.format(self.basepath, template)
        self.path = path
        self.originalFile = File(path)
        self.file = self.originalFile.createTempCopy()

    def isPlaced(self):

    def place(self, variables):
        self.file.replaceVariables(variables)
        targetPath = '{}/{}.{}'.format(self.gitDir, self.template,self.type)
        self.file.copy(targetPath)
        final = File(targetPath)
        final.makeExecutable()

    def enable(self):
        targetPath = '{}/{}.{}'.format(self.gitDir, self.template,self.type)
        githook = File(targetPath)
        githook.makeExecutable()

    def disable(self):
        targetPath = '{}/{}.{}'.format(self.gitDir, self.template,self.type)
        githook = File(targetPath)
        githook.undoExecutable()
