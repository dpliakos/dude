class Variable:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        name  = '{}'.format(self.name)
        string = '{}: {}'.format(name, self.value)
        return string

    def getName(self):
        return self.name

    def getValue(self):
        return self.value

    def getVariable(self):
        return {
            "name": self.name,
            "value": self.value
        }
