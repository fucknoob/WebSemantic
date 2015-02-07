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



pool2 = ConnectionPool('MINDNET', ['localhost:9160'],timeout=10000)

tb_object_3 = pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT3') 


def clear_tables():# limpar as tabelas para iniciar a indexacao
 tb_object_dt3 = pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT_DT3_1_4') 
 tb_object3 = pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT3_1_4') 
 tb_object_relaction3 = pycassa.ColumnFamily(pool2, 'SEMANTIC_RELACTIONS3_1_4') 
 #======================
 tb_object3.truncate()
 tb_object_dt3.truncate()
 tb_object_relaction3.truncate()
 #======================


def run(_id): 
 cmd='apy SemaIndexerStage2.py "igor.moraes"  "'+_id+' defs-interact-classify-detect. "  "client-ecomm-classify-prod-com"  "0" '
 os.system(cmd)
 
 
def get_to_index():
  rg=tb_object_3.get_range()
  #
  cnt=0
  for ky,col in rg:
     id_pg=ky
     try:
      processed=col['processed']
     except:
      processed='N'
     if processed =='S' or processed =='S2' or processed =='E2': continue 
     #
     col['processed']='S'
     tb_object_3.insert(ky,col)
     #
     run(str(id_pg))
     #
     cnt+=1
     #if cnt >= 1: break
  return cnt
                              
    
clear_tables()    
    
rc=get_to_index()

#while rc > 0:
#  rc=get_to_index()
 
print 'All.pg.processed(',rc,')!!!' 