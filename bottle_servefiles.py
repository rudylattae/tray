import os
from bottle import Bottle, static_file
import bottle


# default configuration
_config = {
    'root_dir': None,
}


class Controller:
    """The application controller"""
    def __init__(self, config):
        if not os.path.exists(config['root_dir']):
            raise Exception("Crap")
        self.root_dir = config['root_dir']
    
    def process(self, filename):
        return static_file(filename, root=self.root_dir)
        

def create_app(config={}):
    """App factory. Builds an instance of the app 
    passing it the config that is provided.
    Since the app object that is created is scoped only to this 
    function, it is possible to have multiple instances that do 
    not mess with each other."""
    cfg = _config.copy()
    cfg.update(config)
    
    app = Bottle()
    ctrl = Controller(cfg)
    
    @app.route('/:filename#.+#')
    def process(filename):
        """Locally scoped proxy for the actual controller action we 
        wish to call. This evil hack is needed because of functools' 
        poor implementation of update_wrapper. 
        See: 
         - https://github.com/defnull/bottle/issues/223
         - http://bugs.python.org/issue3445"""
        return ctrl.process(filename)
        
    return app

    
def main(argv):
    if len(sys.argv) > 1:
        root_dir = os.path.abspath(sys.argv[1])
    else:
        root_dir = os.path.abspath('.')
    
    print 'serving files in: ', root_dir
    app = create_app({'root_dir': root_dir})
    bottle.run(app)

    
if __name__ == '__main__':
    import sys
    main(sys.argv)
    
