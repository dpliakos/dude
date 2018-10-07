import yaml

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

class YamlParser(object):

    def __init__(self):
        pass

    def read(self, path):
        raw_data = self.rawRead(path)
        content = []

        for field in raw_data:
            bundle = {
                "field": field,
                "content": raw_data[field]
            }
            content.append(bundle)

        return content

    def rawRead(self, path):
        with open(path, "r") as stream:
            try:
                file = yaml.load(stream)
            except yaml.YAMLError as exc:
                print(exc)

        return file

    '''
    content must by an array of dictionaries.
    The dictionaries may have any (valid) yaml format, they will be
    traversed and be print.
    '''
    def write(self, path, content):
        formated = self.prepareYaml(content)

        with open (path, 'w') as file:
            for line in formated:
                file.write(line)

    def writePreformated(self, path, content):
        with open (path, 'w') as file:
            file.write(content)

    def prepareYaml(self, data):
        formated = self.yamlParse([], 0, data)
        return formated

    def yamlParse(self, accumulator, intent, data):
        if self.isAtomic(data):
            accumulator.append('{}{}'.format(('  '*intent), data))
            return accumulator
        elif type(data) == list:
            for item in data:
                accumulator.append('{}- {}\n'.format(("  "*intent), item))
            return accumulator
        elif type(data) == dict:
            for key in data:
                accumulator.append('\n\n{}{}:\n'.format(("  "*intent), key))
                accumulator = accumulator + self.yamlParse([], intent + 1, data[key])
            return accumulator


        else:
            raise Exception

    def isAtomic(self, data):
        if type(data) == int:
            return True
        elif(type(data) == str):
            return True
        return False
