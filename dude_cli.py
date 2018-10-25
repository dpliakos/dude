from dude import Dude

class DudeCLI:
    def __init__(self):
        self.dude = Dude()

    def invoke(self):
        # print('\nCreating a project')
        # prj = self.dude.createProject(name='dpliakos', path = '/home/dpliakos/Desktop/prj')
        # self.dude.readProjects()

        # self.dude.workon('/home/dpliakos/Desktop/prj')
        # active = self.dude.activeProject

        # active.init()
        # active.open()
        # active.close()

        prj = self.dude.createProject(name='Meridian Trust', path = '/home/dpliakos/Documents/pointBlank/meridian trust/site')
        self.dude.readProjects()

        self.dude.workon('/home/dpliakos/Documents/pointBlank/meridian trust/site')
        active = self.dude.activeProject

        active.init()
        active.open()
        active.close()


    def parseArgs(self):
        pass

if __name__ == '__main__':
    cli = DudeCLI()
    cli.invoke()
