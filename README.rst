========
Overview
========

**Tray** is a minimalistic static file server built with the 
bottle micro web-framework.

Tray is also a simple WSGI app that can be mounted into any 
bottle.py powered app in order to serve static files from any url.

For instance in a regualar bottle.py app you may have the code below 
to serve static files::

    from bottle import route
    import bottle
    
    ...
    
    @route('/static/<path:path>')
    def static(path):
        bottle.static_file(path, root=...)

With tray you would do the following::

    import bottle
    
    ...
    
    myapp = bottle.default_app()
    myapp.mount(bottle.load_app('tray'), '/media')
    bottle.run(app=myapp)
    
It doesn't look like much, but with a pluggable app, it now becomes 
possible to configure the application (e.g. set the "root" directory) 
per mounted instance of the static file handler!


Features
========

    TODO


Installation
============

You can install tray with these commands::

    > pip install tray

If you do not have pip, you may download the source distribution archive. 
Extract it and run::

    > python setup.py install

-----

Copyright (c) 2011 - Rudy Lattae. Released under the New BSD License.