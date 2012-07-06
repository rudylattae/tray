import os
from setuptools import setup

version = '0.4.0dev'
long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CHANGES.txt').read()
])

setup(
    name = "waitless",
    version = version,
    description = "A bottle-wsgi pluggable app that serves static files for",
    long_description = long_description,
    author = "Rudy Lattae",
    author_email = "rudylattae@gmail.com",
    url = 'https://bitbucket.org/rudylattae/bottle-servefiles',
    license = "Simplified BSD",
    keywords = ['bottle', 'bottle.py', 'static', 'file', 'files', 'web', 'app'],
    classifiers = [
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
    py_modules = ['waitless'],
    zip_safe = False,
    install_requires = ['bottle'],
)