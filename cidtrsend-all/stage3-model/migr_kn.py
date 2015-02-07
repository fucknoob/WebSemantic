#coding: latin-1

import base64
import calendar
import os
import rfc822
import sys
import tempfile
import textwrap
import time
import urllib
import urllib2
import urlparse
import thread
 
import subprocess
import string

import BeautifulSoup
 

arrno=[]


import pycassa
from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily

pool2 = ConnectionPool('MINDNET', ['79.143.185.3:9160'],timeout=100000)
tab2 = pycassa.ColumnFamily(pool2, 'web_know')

pool2c = ConnectionPool('MINDNET', ['91.205.172.85:9160'],timeout=10000)

tab2c = pycassa.ColumnFamily(pool2c, 'web_know')

rg=tab2.get_range()
cntk=0
for ky,cls in rg:
 cntk+=1
 #
 tab2c.insert(ky,cls)
 if cntk % 10000 == 0: print 'cnt:',cntk


