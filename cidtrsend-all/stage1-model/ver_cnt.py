#coding: latin-1
# prepara os produtos para ser processados e gerar base de dados
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
import umisc 
import bitly

import xml.dom.minidom 

import pycassa
from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily
from pycassa import index


tp=input('input index web_Cache:')

ver=str(tp)

pool2 = ConnectionPool('MINDNET', ['79.143.185.3:9160'],timeout=10)
wb2 = pycassa.ColumnFamily(pool2, 'web_cache3') 

 
if True:
 rg=wb2.get_range() 
 #
 cnt=0
 for ky,col in rg:
   cnt+=1
   if str(cnt) == ver:
    print 'ky:',ky
    print 'col:',col
    break

 
