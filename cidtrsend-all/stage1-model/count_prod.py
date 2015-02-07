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


pool2 = ConnectionPool('MINDNET', ['79.143.185.3:9160'],timeout=10)
tab2 = pycassa.ColumnFamily(pool2, 'cache_products')
 
if True:
 cl4 = index.create_index_expression(column_name='INDEXED', value='S')
 clausec = index.create_index_clause([cl4],count=100)
 rg=tab2.get_indexed_slices(clausec)  
 #
 cnt=0
 for ky,col in rg:
  cnt+=1
  
 print 'cnt:',cnt 

 
