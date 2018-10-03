import os
import yaml
from ..utils.yaml_parser import YamlParser
from ..variable.variable import Variable

class Project():
    def __init__(self, name, path, init):
        self.defaultProjectFile = "dude.yml"
        self.name = name
        self.initMethod = init
        self.gitHooks = []
        self.path = path
        self.variables = []
        self.initialized = False
        self.filePath = "/".join([self.path, self.defaultProjectFile])
        self.isFileCreated = os.path.isfile(self.filePath)

    def __repr__(self):
        line = ''
        line += 'name: '  + self.name + '\n'
        line += 'path: ' + self.path + '\n'
        if len(self.gitHooks) > 0:
            line += 'git hooks: \n'
            for hook in self.gitHooks:
                line += '\t' +  hook + '\n'

        if len(self.variables) > 0:
            line += 'variables: \n'
            for var in self.variables:
                line += "\t" +  var + ": " + self.variables[var] + "\n"

        return line

    def getProject(self):
        project = {
            "name": self.name,
            "init": self.initMethod,
            "path": self.path
        }

        return project

    def readFromDb(self, db):
        if not self.initialized:
            print ('Project is not initialized yet')
            return False

        query = """ select * from projects where path = '{}' """.format(self.path)
        return db.fetch(query)

    def discover(self):
        filePath = "/".join([self.path, self.defaultProjectFile])

        with open(filePath, "r") as stream:
            file = yaml.load(stream)

        if "name" in file:
            self.name = file["name"]
        if "init" in file:
            self.initMethod = file["init"]
        if "hooks" in file:
            self.gitHooks = file["hooks"]
        if "variables" in file:
            for variable in file['variables']:
                var = Variable(variable, file['variables'][variable])
                self.variables.append(var)

        self.initialized = True

    def create(self):
        if not self.isFileCreated:
            data = self.getProject()
            yaml = YamlParser()
            yaml.write(path=self.filePath, content=data)

    def readFile(self):
        print  ('reading the configuration file')

    def save(self, db):
        if not self.initialized:
            print('The project is not ready yer')
            return False

        project = self.getProject()
        projectId = db.insert('projects', project)

        # for variable in self.variables:
        #
        #     bundle = {
        #         "title": variable,
        #         "value": self.variables[variable],
        #         "project": str(projectId)
        #     }
        #     db.insert('variables', bundle)

        for hook in self.gitHooks:
            bundle = {
                "hook": str(1),
                "project": str(projectId)
            }

            db.insert('githook_assignments', bundle)

    def addVariable(self, title, value):
        pass

    def setup(self):
        pass
