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

    print('\n\nReading projects')
    dude.readProjects()
    print('\nCreating a project')
    prj = dude.createProject(name='dpliakos', path = '/home/dpliakos/Desktop/prj', method='default')
    # prj2 = dude.createProject(name='dpliakos2', path = '/home/dpliakos/Desktop/prj2', method='default')
    print ('\nReading projects again')
    dude.readProjects()

    dude.workon('/home/dpliakos/Desktop/prj')
    test = dude.activeProject

    test.addVariable('__another__', 'test')
    # test.addVariable('__lala__', 'another test')
    # test.addVariable('__test__', 'this is a test var')

    dude.readProjects()

    print (test.variables)
