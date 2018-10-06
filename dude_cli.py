from dude import Dude

class DudeCLI:
    def __inti__(self):
        print('cli init!')

if __name__ == '__main__':
    dude = Dude()
    try:
        dude.clean()
    except:
        pass

    dude.install()

    print('\nCreating a project')
    prj = dude.createProject(name='dpliakos', path = '/home/dpliakos/Desktop/prj')
    dude.readProjects()

    dude.workon('/home/dpliakos/Desktop/prj')
    test = dude.activeProject
    
