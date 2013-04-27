#!/usr/bin/python
import os
here = lambda x: os.path.join(os.path.abspath(os.path.dirname(__file__)), x)

os.system('rsync --delete -v -r %s projects@home.stephane-klein.info:www/trm/' % here('./build/html/'))
