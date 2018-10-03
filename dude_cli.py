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
    prj = dude.createProject(name='dpliakos', path = '/home/dpliakos/Desktop/prj2', method='default'   )
    # print ('\nReading projects again')
    # dude.readProjects()

    dudeDB = dude.getDB()

    print (prj.readFromDb(dudeDB))
    # prj.create()
