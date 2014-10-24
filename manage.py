'''
Created on Oct 17, 2014

@author: ayan
'''
from flask.ext.script import Manager, Command, Option
from flask.ext.collect import Collect
from pubs_ui import app as application


class RunServer(Command):
    """
    Run flask development server
    """
    
    option_list = (
                   Option('--port', '-p', dest='port'),
                   )
    
    def run(self, port):
        if port:
            application.run(port=int(port))
        else:
            application.run()


class CollectStaticFiles(Command):
    """
    collects static files
    so Apache can serve them
    """ 
    
    def run(self):
        collect = Collect()
        collect.init_app(application)
        collect.init_script(manager)
        collect.collect(verbose=True)


manager = Manager(application)
manager.add_command('collect', CollectStaticFiles())


if __name__ == '__main__':
    manager.run()