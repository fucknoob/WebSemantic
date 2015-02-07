# rastrea td o web_cache e retorna os id dos objetos cadastrados e executa etapa 1

import sys
import os
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

import logging
from StringIO import StringIO

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('pblnksExtra')


ch  = logging.StreamHandler ()
lbuffer = StringIO ()
logHandler = logging.StreamHandler(lbuffer)

log.addHandler(logHandler) 
log.addHandler(ch) 



pool2 = ConnectionPool('MINDNET', ['localhost:9160'],timeout=10)
#
wb2 = pycassa.ColumnFamily(pool2, 'web_cache1') # lugar para indexar 


def clear_tables():# limpar as tabelas para iniciar a indexacao
 s=wb2.get_range()
 for ky,col in s:
  col['indexed']='N'
  wb2.insert(ky,col)


def run(id): 
 cmd='apy SemaIndexerStage1.py "igor.moraes" "parse-learn-product" "'+id+'"  '
 os.system(cmd)
 
 
all_index=0  
def get_to_index():
  global all_index
  cl4 = index.create_index_expression(column_name='indexed', value='N')
  clausec = index.create_index_clause([cl4],count=10) 
  rg=wb2.get_indexed_slices(clausec)  
  #
  cnt=0
  for ky,col in rg:
    id_pg=ky
    col['indexed']='S'
    wb2.insert(ky,col)
    #
    run(str(id_pg))
    #
    cnt+=1
    print 'page:',all_index
    all_index+=1
  return cnt
                              
    
    
#=======================
clear_tables()
#=======================
rc=get_to_index()
while rc > 0:
  rc=get_to_index() 
 
print 'All.pg.processed!!!' 