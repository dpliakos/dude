class Variable:
    def __inti__(self, project):
        self.name = ''
        self.value = ''
        self.project = ''

    def __repr__(self):
        return self.name + " = " + self.value + " (for " + self.project + ")"

    def getName(self):
        return self.name

    def getValue(self):
        return self.value

    def getProject(self):
        return self.project

    def getVariable(self):
        return {
            "name": self.name,
            "value": self.value,
            "application": self.application
        }
