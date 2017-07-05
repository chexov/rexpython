from distutils.core import setup

setup(
    name='rexpython',
    version='0.1.8',
    author='Anton P. Linevich',
    author_email='anton@linevich.com',
    packages=['rexpython', "tblib", ],
    scripts=[],
    url='http://pypi.python.org/pypi/rexpython/',
    license='LICENSE.txt',
    description='simple Rx pipeline implementation',
    long_description=open('README.txt').read(),
    install_requires=[],
)
