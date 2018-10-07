import os
import subprocess as spc

class File:
    def __init__(self, path):
        self.path = path

    def exist(self):
        return os.path.isfile(self.path)

    def copy(self, target):
        copy = spc.call(['cp', self.path, target])
        return copy == 0

    def getMatches(self, target):
        command = '''egrep '{}' {}'''.format(target, self.path)
        egrep = spc.getstatusoutput(command)
        return egrep[1:len(egrep)]

    def matches(self, target):
        status = spc.call(['egrep', target, self.path])
        return status == 0

    def replace(self, source, target):
        regex = 's/{}/{}/g'.format(source, target)
        status = spc.call(['sed', '-i', regex, self.path])
        return status == 0

    def delete(self):
        status = spc.call(['rm', self.path])
        return status

    def makeExecutable(self):
        status = spc.call(['chmod', 'a+x', self.path])
        return status == 0

    def execute(self):
        status = spc.call([self.path])
        return status == 0
