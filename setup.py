
from distutils.core import setup

setup(
    name='mlia',
    version='0.1.0',
    author='Lawrence Allan Jones',
    author_email='mrwizard82d1@earthlink.net',
    packages=['mlia', 'mlia.test'],
    scripts=['bin/mlia.py',],
    url='http://pypi.python.org/pypi/mlia/',
    license='LICENSE.txt',
    description='Useful mlia stuff.',
    long_description=open('README.txt').read(),
    install_requires=['numpy',],
    )
