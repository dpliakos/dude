import os
import subprocess as spc

class Directory:
    def __init__(self, path, autoCreate=False):
        self.path = path

        if not self.exist():
            if autoCreate:
                self.create()
            else:
                print (self.path)
                raise Exception()


    def exist(self):
        exist = os.path.isdir(self.path)
        return exist

    def create(self):
        success = spc.call(['mkdir', self.path])
