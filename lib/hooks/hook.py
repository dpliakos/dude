class Hook:
    def __init__(self, path):
        self.name = ''
        self.role = ''
        self.path = path
        self.variables = {}

    def getName(self):
        return self.name

    def getRole(self):
        return self.role

    
