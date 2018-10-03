import yaml
import sqlite3
from lib.project.project import Project
from lib.db.database import DBManager
from lib.utils.yaml_parser import YamlParser
from lib.utils.compatibility import Compatibility

class Dude:
    def __init__(self):
        self.dbconfiguration = './config/db.yml'
        self.dbInitData = './config/init_data.yml'
        self.stdin = Compatibility()
        self.dbName = '.dude_drupal'
        self.db = DBManager(self.dbName)
        self.installed = True
        self.projects = []

    def checkInstallation(self):
        return self.installed

    def install(self):
        yml = YamlParser()

        dbStructure = yml.read(self.dbconfiguration)
        for bundle in dbStructure:
            self.db.createTable(bundle['field'], bundle['content'])

        dbData = yml.read(self.dbInitData)
        for bundle in dbData:
            for item in bundle['content']:
                self.db.insert(bundle['field'], {'title': item})

        print ('Dude was installed!!')

    def clean(self):
        yml = YamlParser()
        dbStructure = yml.read(self.dbconfiguration)

        for bundle in dbStructure:
            self.db.dropTable(bundle['field'])

        print('tables were deleted')

    def readProjects(self):
        yml = YamlParser()

        dbStructure = yml.read(self.dbconfiguration)
        content = self.db.preview('projects')
        if len(content) > 0:
            for item in content:
                print(item)
        else:
            print ('No project created yet.')

    def say_hello(self):
        print('hello! I\'m Dude!')

    def createProject(self, name='', path='', method=''):

        if name == '':
            print ('Project name: ')
            name = self.stdin.read()

        if path == '':
            print ('Project path: ')
            path = self.stdin.read()

        if method == '':
            print ('InitMethod[default]: ')
            method = self.stdin.read()

        project = Project(name, path, method)
        project.create()
        project.discover()
        project.save(self.db)
        return project

    def getDB(self):
        return self.db
