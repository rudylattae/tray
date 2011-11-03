import os
from bottle import Bottle, static_file
import bottle


# default configuration
_config = {
    'ROOT_DIR': None,
}


class StaticFileRepository:
    """This repository is home to our core business logic"""
    def __init__(self, config):
        if not os.path.exists(config['ROOT_DIR']):
            raise Exception("Crap")
        self.root_dir = config['ROOT_DIR']
    
    def get(self, filename):
        return static_file(filename, root=self.root_dir)
        

def create_app(custom_config=None, app=None):
    """App factory. Builds an instance of the app 
    passing it the config that is provided.
    Since the app object that is created is scoped only to this 
    function, it is possible to have multiple instances that do 
    not mess with each other."""
    config = _config.copy()
    if custom_config: config.update(custom_config)
    if not app: app = Bottle()
    
    repo = StaticFileRepository(config)
    
    @app.get('/:filename#.+#')
    def get(filename):
        """Locally scoped proxy for the actual repo action we 
        wish to call. This evil hack is needed because of functools' 
        poor implementation of update_wrapper. 
        See: 
         - https://github.com/defnull/bottle/issues/223
         - http://bugs.python.org/issue3445"""
        return repo.get(filename)
        
    return app

    
def main(argv):
    if len(sys.argv) > 1:
        root_dir = os.path.abspath(sys.argv[1])
    else:
        root_dir = os.path.abspath('.')
    
    print 'serving files in: ', root_dir
    app = create_app({'ROOT_DIR': root_dir})
    bottle.run(app)

    
if __name__ == '__main__':
    import sys
    main(sys.argv)
    
