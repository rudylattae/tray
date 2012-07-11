import os
from setuptools import setup

version = '0.5.0dev'
long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CHANGES.txt').read()
])

setup(
    name = "tray",
    version = version,
    description = "A basic bottle-wsgi pluggable app that serves static files",
    long_description = long_description,
    author = "Rudy Lattae",
    author_email = "rudylattae@gmail.com",
    url = 'https://github.com/rudylattae/tray',
    license = "Simplified BSD",
    keywords = ['bottle', 'bottle.py', 'static', 'file', 'files', 'web', 'app', 'tray'],
    classifiers = [
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
    py_modules = ['tray'],
    zip_safe = False,
    install_requires = ['bottle'],
    entry_points = {
        'console_scripts': [ 'tray = tray:main' ]
    }
)