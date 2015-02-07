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

sys.path.append('/Neural')

import umisc

 

arrno=[]


import pycassa
from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily

pool2 = ConnectionPool('MINDNET', ['localhost:9160'],timeout=100000)
tab2 = pycassa.ColumnFamily(pool2, 'web_know')

rg=tab2.get_range()
cntk=0
cnt_idx=0
cnt_pg=0
print 'start cnt....'
for ky,cls in rg:
 cntk+=1
 if cls[u'indexed'] == 's':
   cnt_idx+=1
 txt=cls[u'pg']  
 if txt == None : txt=''
 txt=umisc.trim(txt)
 if txt != '':
  cnt_pg+=1
 #
 if cntk % 50000 == 0: 
   print 'cnt-all:',cntk,',cnt-idx:',cnt_idx,',cnt.pg:',cnt_pg
   
   
print 'cnt-all:',cntk,',cnt-idx:',cnt_idx,',cnt.pg:',cnt_pg

