import os
from setuptools import setup

version = '0.1.2dev'
long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CHANGES.txt').read()
])

setup(
    name = "bottle-servefiles",
    version = version,
    description = "A reusable app that serves static files for bottle apps",
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
    py_modules = ['bottle_servefiles'],
    zip_safe = False,
    install_requires = [],
)