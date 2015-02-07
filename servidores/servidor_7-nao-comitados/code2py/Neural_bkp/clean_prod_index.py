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


pool2 = ConnectionPool('MINDNET', ['localhost:9160'],timeout=10)
tab2 = pycassa.ColumnFamily(pool2, 'cache_products')
wb2 = pycassa.ColumnFamily(pool2, 'web_cache3') 

wb2.truncate()
 
if True:
 print 'get.rows....'
 rg=tab2.get_range()
 #
 cnt=0
 for ky,col in rg:
  url=ky
  col['INDEXED']='N'
  tab2.insert(ky,col) 

 
