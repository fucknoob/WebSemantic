#coding: latin-1
# cache_products -> tabela com os links diretos pros produtos, sem paginas intermediarias de links


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

from BeautifulSoup import BeautifulSoup, SoupStrainer
import umisc 
import bitly
import time

import xml.dom.minidom 

import pycassa
from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily
from pycassa import index


import logging
from StringIO import StringIO

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('pblnksSubmarino')


ch  = logging.StreamHandler ()
lbuffer = StringIO ()
logHandler = logging.StreamHandler(lbuffer)

log.addHandler(logHandler) 
log.addHandler(ch) 


pool2 = ConnectionPool('MINDNET', ['79.143.185.3:9160'],timeout=10)
tab2 = pycassa.ColumnFamily(pool2, 'cache_products')
tab3 = pycassa.ColumnFamily(pool2, 'cache_links') # links temporarios


def test_page(url):
 fnd1=False
 try:
   tab3.get(url)
   fnd1=True
 except: fnd1=False
 #==============================
 fnd2=False
 try:
   tab2.get(url)
   fnd2=True
 except: fnd2=False
 if fnd1:
   return 2
 if fnd2:
   return 1  
 #==============================
 try:
  if url.startswith('http://www.submarino.com.br/produto/') or url.startswith('https://www.submarino.com.br/produto/'):
    return 1
  else:
    return 2
 except:  
   return 2 
 
def parse_url(url_entry,base_url):
 collect_u=[]
 opener = urllib2.build_opener()
 opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.2) Gecko/20090729 Firefox/3.5.2 GTB5')]
 data_Res = opener.open(url_entry, '' ).read()
 #======================
 linksf=BeautifulSoup(data_Res, parseOnlyThese=SoupStrainer('a'))
 #print '->',linksf
 for link in linksf:
    #print 'process.url:',link
    if link.has_key('href'):
      if link['href'] != '#':
       strcmps=''+link['href']
       try:
        if strcmps != '':
         if (strcmps[0] == '/' and strcmps[1] == '/') or (not strcmps.startswith('http:')) :
          #print 'url.skip:', 'http:'+strcmps.encode('latin-1')
          pass
         else:
          #print strcmps
          if strcmps[0] != '#':
           url_c=strcmps.encode('latin-1')
           if url_c.upper().find(base_url.upper())>-1 or url_c.upper().startswith('http://www.submarino.com.br/produto/'.upper()):
             collect_u.append(url_c)
       except Exception,e:
            print 'string:',strcmps
            print 'Error:',e            
 print 'url(',len(collect_u),'):',url_entry           
 return collect_u



def parse_url_rt(url):
 return url
 #================
 rt=''
 ind=0
 for u in url:
  if u == '?' and url[ind-4:4] == 'html'  : break
  rt+=u
 return rt

def run_process():
 def post_urls(r):
   for lnk in r:
    lnk=parse_url_rt(lnk)
    rt=test_page(lnk)
    if rt==1: # grava tab cache_products
      try:
        # verifica se tem no banco de dados
        r=tab2.get(lnk)
      except:
       # se nao tiver, insere
       print 'insert into product.table:',lnk
       try:
         tab2.insert(lnk,{"INDEXED":'N'})
       except :
         log.exception("ERROR")         
        
    else:# grava tab cache_links
      try:
        # verifica se tem no banco de dados
        r=tab3.get(lnk)
      except:
       # se nao tiver, insere
       print 'insert into link.table:',lnk
       tab3.insert(lnk,{"INDEXED":'N'})
 def empty_links():
  r=tab3.get_range()
  for c,i in r:
   return False
  return True
 if empty_links(): 
   print 'init cache links...'
   #
   lnk_entrada='http://www.submarino.com.br/loja/342768/moda-calcados-e-acessorios?sc_m=in|bf|moda|_'
   base_url='moda-calcados-e-acessorios'
   r=parse_url(lnk_entrada,base_url)
   post_urls(r)
   return True
 else: # open table links an run each link     
       # get INDEXED = 'N'  in cache_links
       print 'implement cache links...' 
       base_url='moda-calcados-e-acessorios'
       cl4 = index.create_index_expression(column_name='INDEXED', value='N')
       clausec = index.create_index_clause([cl4],count=100)
       resultSet=tab3.get_indexed_slices(clausec)  
       have=False
       for key1,results in resultSet:
         link=key1
         print 'run.url:',link
         rt=parse_url(link,base_url)
         post_urls(rt)
         have=True
       return have  
         
         
hv=run_process() 
while hv:
   time.sleep(1)
   hv=run_process()
      
