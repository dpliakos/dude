from datetime import datetime
from ..utils.file import File
from ..utils.directory import Directory

class Script():
    def __init__(self, name, basepath, basetarget):
        self.basepath = basepath

        baseDir = Directory(basepath)

        self.path = '/'.join([self.basepath, name])
        self.file = File(self.path)

        self.basetarget = basetarget
        targetDir = Directory(basetarget, True)

        if not targetDir.exist():
            targetDir.create()

        time = str(datetime.now()).replace(' ', '_').replace(':', '-').split('.')[0]

        self.newName = '{}_{}'.format(time, name)
        exists = self.file.exist()

        self.tmpPath = '/'.join([self.basetarget, self.newName])
        self.tmpFile = None

        if not exists:
            raise Exception()



    def createTempCopy(self):
        success = self.file.copy(self.tmpPath)
        self.tmpFile = File(self.tmpPath)

    def deleteTempCopy(self):
        success = self.tmpFile.delete()
        self.tmpFile = None

    def neededVariables(self, variables):
        matches = []

        for key in variables:
            match = self.tmpFile.getMatches(key)
            if (match[0] != ''):
                matches.append(match)

    def replaceVariables(self, variables):
        for key in variables:
            self.tmpFile.replace(key, variables[key])

    # TODO: remove this function
    def execute(self):
        self.tmpFile.makeExecutable()
        self.tmpFile.execute()
