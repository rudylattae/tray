========
Overview
========

**bottle-servefiles** can serve static files for your bottle.py application.

I deceided to create this application to further my understanding 
of WSGI and how to build pluggable apps for the bottle.py ecosystem.

bottle-servefiles aims to be a simple WSGI app that can be mounted into any 
bottle.py powered app in order to serve static files from any url.

For instance in a regualar bottle.py app you may have the code below 
to serve static files::

    from bottle import route
    import bottle
    
    ...
    
    @route('/static/:filename#.*#')
    def static(filename):
        bottle.static_file(filename, root=...)

What I would like is to be able to mount a reusable static file handler 
on any path I chose within my application, without having to explicitly 
attach the path to the handler definition.

Ok I know that is pure nonsense but I had to come up with a compelling 
reason to build this thing in the first place.

So moving swiftly forward, with a static handler implemented as a 
pluggable bottle app, I would be able to do the following::

    import bottle
    
    ...
    
    myapp = bottle.default_app()
    myapp.mount(bottle.load_app('servefiles'), '/media')
    bottle.run(app=myapp)
    
It doesn't look like much, but with a pluggable app, it now becomes 
possible to configure the application (e.g. set the "root" directory) 
per mounted instance of the static file handler!


Features
========

    TODO


Installation
============

You can install upgrade or uninstall bottle-servefiles with these commands::

    > pip install bottle-servefiles
    > pip install -U bottle-servefiles
    > pip uninstall bottle-servefiles

If you do not have pip you may use easy install::

    > easy_install bottle-servefiles

If you do not have easy_install, you may download the piot 
source distribution archive. Extract it and run::

    > python setup.py install


Example usage 
=============

This is a basic outline of how you would use bottle-servefiles 
to server static files from your application.

Create an application module "app.py" with the contents::

    import bottle
    
    
    class MySite(object):
        def __init__(self, app=None):
            self.app = app if app else bottle.default_app()
    
        def __call__(self, environ, start_response):
            return self.app(environ, start_response)
    
    
    if __name__ == '__main__':
        mysite = MySite()
        mysite.app.mount(bottle.load_app('servefiles'), '/__media')
        bottle.debug(True)
        bottle.run(app=foo, reloader=True)
    


-----

Copyright (c) 2011 - Rudy Lattae. Released under the New BSD License.