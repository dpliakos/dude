import os

class Directory:
    def __init__(self, path):
        self.path = path

        if not self.exist():
            raise Exception()


    def exist(self):
        exist = os.path.isdir(self.path)
        return exist
