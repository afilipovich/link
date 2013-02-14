# -*- coding: utf-8 -*-
"""
link
~~~~~~~~~~~~

The link module helps you connect to all of the data sources you need through a
simple configuration 
    
Sample Config to connect to mysql::

   { 
        "dbs":{
           "my_db": {
               "wrapper": "MysqlDB",
               "host": "mysql-master.123fakestreet.net",
               "password": "<password>",
               "user": "<user>",
               "database": "<database_name>"
           }
        }
    }

Sample Code::

    In [3]: from link import lnk
    
    # uses the keys from your configuration to look up and create the
    # appropriate objects
    In [35]: my_db = lnk.dbs.my_db

    In [36]: data = my_db.select('select id from my_table')

:copyright: (c) 2013 by David Himrod
:license: Apache2, see LICENSE for more details.

"""
#import all of this version information
__version__ = '0.1.4'
__author__ = 'David Himrod'
__license__ = 'Apache 2.0'
__copyright__ = 'Copyright 2013 David Himrod'
__title__ = 'link'

lnk = None
#i don't like this but i can't figure out a better way to do it yet
try:
    from .link import Link, Wrapper, lnk
except:
    pass

from common import *
