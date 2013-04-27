import os
import sys

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen  # NOQA

print("""
This bootstrap install virtualenv instance in your working folder (%s).
Warning : this file isn't buildout bootstrap.py
""" % os.getcwd())

sys.argv = ['bootstrap.py', '.']
exec(
    urlopen('https://raw.github.com/pypa/virtualenv/develop/virtualenv.py').read()
)

print("""

Next :

    $ bin/pip install -r requirements.txt; bin/pip install https://github.com/harobed/matplotlib/archive/master.zip

""")
