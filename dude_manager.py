from dude import Dude
from dude_cli import DudeCLI

class DudeManager():
    def __init__(self):
        self.dude = Dude()
        self.dudeIsInstalled = self.dude.checkInstallation()

    def installDude(self):
        self.dude.install()

    def removeDude(self):
        self.dude.clean()

    def updateDude(self):
        print ('no update functionality yet!')
        pass

if __name__ == '__main__':
    manager = DudeManager()

    if not manager.dudeIsInstalled:
        user = input('Dude is not installed. Do you want to install it?[y/n] ')
        if user == 'y' or user == 'Y':
            manager.installDude()

    DudeCLI().invoke()
