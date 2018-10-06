import os
import yaml
from ..utils.yaml_parser import YamlParser
from ..variable.variable import Variable

class Project():
    def __init__(self, name, path, init, db=None):
        self.defaultProjectFile = "dude.yml"
        self.name = name
        self.initMethod = init
        self.gitHooks = []
        self.path = path
        self.variables = []
        self.initialized = False
        self.filePath = "/".join([self.path, self.defaultProjectFile])
        self.isFileCreated = os.path.isfile(self.filePath)
        self.db = None
        self.id = None

        if db is not None:
            print ('has db')
            self.db = db
            self.id = self.existsInDb(self.db)

        if self.isFileCreated:
            self.discover()

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
                line += '\t {}: {}\n'.format(var.name, var.value)

        return line

    def getProject(self):
        project = {
            "name": self.name,
            "init": self.initMethod,
            "path": self.path
        }

        if len(self.variables) > 0:
            project['variables'] = self.variables

        return project

    def existsInDb(self, db):
        query = 'select id from projects where path = "{}"'.format(self.path)
        result = db.fetch(query)

        if len(result) > 0:
            id  = result[0][0]
            print ('result')
            print (result)
            print ('id = {}'.format(id))
            return id
        else:
            return None

    def readFromDb(self, db):
        if not self.initialized:
            print ('Project is not initialized yet')
            return False

        query = """ select * from projects where path = '{}' """.format(self.path)
        return db.fetch(query)

    def createToDb(self, db):
        project = {
            "name": self.name,
            "init": self.initMethod,
            "path": self.path
        }

        id = db.insert('projects', project)
        self.id = id

        for variable in self.variables:

            bundle = {
                "title": variable.name,
                "value": variable.value,
                "project": str(id)
            }

            db.insert('variables', bundle)

    def saveToDb(self, db):
        pass

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
                for key in variable:
                    var = Variable(key, variable[key])
                    self.variables.append(var)

        self.initialized = True

    def create(self):
        # if not self.isFileCreated:
        data = self.getProject()
        yaml = YamlParser()
        yaml.write(path=self.filePath, content=data)

    def readFile(self):
        print  ('reading the configuration file')

    def saveFile(self):
        data = self.getProject()
        yaml = YamlParser()
        yaml.write(path=self.filePath, content=data)

    def save(self, db):
        # check if exists in DB
        if not self.initialized:
            print('The project is not ready yet')
            return False


        id = self.existsInDb(db)
        if id is None:
            self.createToDb(db)
        else:
            self.saveToDb(db)

        # for variable in self.variables:
        #
        #     bundle = {
        #         "title": variable.name,
        #         "value": variable.value,
        #         "project": str(projectId)
        #     }
        #     db.insert('variables', bundle)
        #
        # for hook in self.gitHooks:
        #     bundle = {
        #         "hook": str(1),
        #         "project": str(projectId)
        #     }
        #
        #     db.insert('githook_assignments', bundle)

    def addVariable(self, name, value):
        found = False

        for variable in self.variables:
            if variable.name == name:
                found = True

        if not found:
            variable = Variable(name, value)
            self.variables.append(variable)
            self.create()

    def removeVarible(self, name):
        newVars = []
        variableFound = False
        for variable in self.variables:
            if variable.name != name:
                newVars.append(variable)
            else:
                variableFound = True
        self.variables = newVars

        self.create()
        return variableFound

    def setup(self):
        pass

    def variablesChanged(self, database=None):
        db = None
        if database is not None:
            db = database
        elif self.db is not None:
            db = self.db
        else:
            raise Exception()

        query = 'select title, value from variables where id = {}'.format(self.id)
        print (query)
        dbVars = db.fetch(query)
