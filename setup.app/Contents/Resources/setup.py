"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['zeloxa.py']
DATA_FILES = [
	('', ['assets']),
	('', ['zeloxa.icns'])

]
OPTIONS = {
	'argv_emulation': True,
	'iconfile': 'zeloxa.icns'
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
