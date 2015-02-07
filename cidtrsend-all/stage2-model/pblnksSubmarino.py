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

import logging
from StringIO import StringIO

import umisc

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('pblnksExtra')


ch  = logging.StreamHandler ()
lbuffer = StringIO ()
logHandler = logging.StreamHandler(lbuffer)

log.addHandler(logHandler) 
log.addHandler(ch) 



pool2 = ConnectionPool('MINDNET', ['79.143.185.3:9160'],timeout=100000)
tab2 = pycassa.ColumnFamily(pool2, 'cache_products')
wb2 = pycassa.ColumnFamily(pool2, 'web_cache1') # lugar para indexar 
 

#start -> inicio da faixa de ID 
start=10000
 
 
def short_url(urllong):
 try:
  rs= bitly.short_url(urllong)
 except:
  try:
   rs= bitly.short_url(urllong)
  except:
   try:
    rs= bitly.short_url(urllong)
   except:
     return ''     
 return rs
 
def lomadeezar_links(links_tw):
 areturn=[]
 lnk=[]
 ind=1
 #if len(links_tw)==0: return []
 for l in links_tw:
   #l=urllib.quote(l)
   lnk.append(['link'+str(ind),l])
   ind+=1
 url='http://ws.buscape.com/service/createLinks/lomadee/564771466d477a4458664d3d/?'
 #url='http://sandbox.buscape.com/service/createLinks/lomadee/564771466d477a4458664d3d/?' 
 args = {}  
 print 'process links to lomadee:',len(links_tw) 
 args['sourceId']='28009381'
 for ul in lnk:
   args[ul[0]]=ul[1]
 dt=urllib.urlencode(args)    
 file = urllib2.urlopen(url,dt)
 data_Resk = file.read()
 #print data_Resk
 dom2 = xml.dom.minidom.parseString(data_Resk)
 nods=dom2.childNodes
 for n1 in nods:
  n2=n1.getElementsByTagName('lomadeeLinks')
  if n2 != None:
   found_elems=False
   found_elem1=False
   for n3 in n2:
    n4=n3.getElementsByTagName('lomadeeLink')
    for n5 in n4:
     args={}
     found_elems=True
     for n6 in n5.getElementsByTagName('originalLink'):
      args['originalLink']=n6.firstChild.data
     for n7 in n5.getElementsByTagName('redirectLink'): 
      args['redirectLink']= n7.firstChild.data
      found_elem1=True
     for n8 in n5.getElementsByTagName('code'): 
      args['code']= n8.firstChild.data
     for n9 in n5.getElementsByTagName('id'): 
      args['id']= n9.firstChild.data
     areturn.append(args)
   if not found_elems or not found_elem1:
     print 'Lomadee error(1):',data_Resk,'\n',dt  
 # 
 # 
 return areturn
 
 
def parse_url_rt(url):
 rt=''
 for u in url:
  if u == '?': break
  rt+=u
 return rt

def parse_metas(soup):
 def s_sanity(st):
  r=''
  ant=''
  for i in st:
   if i == ' ' and ant == ' ':
    continue
   else:
     r+=i
   ant=i  
  return r   
 rt=[] 
 # parse html itens 
 descr_P=''.encode('latin-1','ignore')
 descr_All=soup.findAll("h1",attrs={'class':'title-product'})
 for ds in descr_All:
  for d in ds.contents:
   tx=''
   if type(d).__name__ == 'Tag':
    tx= d.getText(' ').encode('latin-1', 'ignore')
   if type(d).__name__ == 'NavigableString':
    tx=d.encode('latin-1', 'ignore')
   descr_P+=' '+tx
 #sanity descr_P
 descr_P=s_sanity(descr_P) 
 rt.append(['descricao',descr_P])
 # preco
 descr_P=''.encode('latin-1','ignore')
 descr_All=soup.findAll("span",attrs={'class':'amount'})
 rfir=True
 for ds in descr_All:
  descr_P=''
  for d in ds.contents:   
   tx=''
   if type(d).__name__ == 'Tag':
    tx= d.getText(' ').encode('latin-1', 'ignore')
   if type(d).__name__ == 'NavigableString':
    tx=d.encode('latin-1', 'ignore')
   descr_P+=' '+tx
  descr_P=s_sanity(descr_P) 
  if rfir:
   rt.append(['preco base',descr_P])
  else:
   rt.append(['preco atual',descr_P])
  rfir=False 
 # fotos
 descr_P=''.encode('latin-1','ignore')
 descr_All=soup.findAll("figure",attrs={'class':'main-product-photo'})
 rfir=True
 for ds in descr_All:
  descr_P=''
  for d in ds.contents:
   try:
    if d.has_key('href'):
     tx=d['href']
     rt.append(['##image',tx])
   except:
     pass
  rfir=False 
  

 # parse categoria
 categ=soup.findAll("span",attrs={'class':'span-bc'})
 caracts_cateh=[]
 cats=[]
 atct=False
 for ittb in  categ:
   lnc=len(ittb.contents)
   matrizc=[]
   for elm in ittb.contents:
    if getattr(elm, 'name', None) == 'a':
       tx=''
       if type(elm).__name__ == 'Tag':
        tx=elm.getText(' ').encode('latin-1', 'ignore')
       if type(elm).__name__ == 'NavigableString':
        tx=elm.encode('latin-1', 'ignore')
       tx=tx.replace(' - ','\n') 
       tx=umisc.trim(tx)
       if tx.startswith('Moda'):
         atct=True
       if atct:         
         matrizc.append(tx)
   if len(matrizc) > 0:
     cats=(matrizc)   
   if len(cats)>0:
    caracts_cateh.append(cats)
    cats=[]
 # parse caracts table
 rt2=[] 
 rt2.append(caracts_cateh) 
 matrizcG=[]
 matrizc=[]
 tbs_ln=soup.findAll("table",attrs={'class':'ficha-tecnica'} )
 for ittb in  tbs_ln:
    for elm in ittb.contents:
     if getattr(elm, 'name', None) == 'tr':
      tx1=''
      tx2=''
      try:
       ak=elm.contents     
      except:
       continue
      for elm2 in elm.contents:
         if getattr(elm2, 'name', None) == 'th':
          for dt1 in elm2.contents:
            tx=''
            if type(dt1).__name__ == 'Tag':
             tx=dt1.getText(' ').encode('latin-1', 'ignore')
            if type(dt1).__name__ == 'NavigableString':
             tx=dt1.encode('latin-1', 'ignore')
            tx=tx.replace(' - ','\n') 
            tx=umisc.trim(tx)
            if len(tx)>0:
             if tx[0] == '\n':
              tx=tx[1:]
             tx=umisc.trim(tx)
             if tx[0] == '\r':
              tx=tx[1:]
             tx=umisc.trim(tx)
             if tx[-1] == '\r':
              tx=tx[:-1]
             #============================= 
             tx=umisc.trim(tx)
             if tx[0] == '\n':
              tx=tx[1:]
             tx=umisc.trim(tx)
             if tx[0] == '\r':
              tx=tx[1:]
             tx=umisc.trim(tx)
             if tx[-1] == '\r':
              tx=tx[:-1]
             #============================= 
            tx1+=s_sanity(tx)
         if getattr(elm2, 'name', None) == 'td':
          for dt2 in elm2.contents:
            tx=''
            if type(dt2).__name__ == 'Tag':
             tx=dt2.getText(' ').encode('latin-1', 'ignore')
            if type(dt2).__name__ == 'NavigableString':
             tx=dt2.encode('latin-1', 'ignore')
            tx=tx.replace(' - ','\n')
            tx=umisc.trim(tx)
            if len(tx)>0:
             if tx[0] == '\n':
              tx=tx[1:]
             tx=umisc.trim(tx)
             if tx[0] == '\r':
              tx=tx[1:]
             tx=umisc.trim(tx)
             if tx[-1] == '\r':
              tx=tx[:-1]
             #============================= 
             tx=umisc.trim(tx)
             if tx[0] == '\n':
              tx=tx[1:]
             tx=umisc.trim(tx)
             if tx[0] == '\r':
              tx=tx[1:]
             tx=umisc.trim(tx)
             if tx[-1] == '\r':
              tx=tx[:-1]
             #============================= 
            tx2+= s_sanity(tx) 
      if tx1 != '' and tx2 != '' :   
        matrizc.append([tx1,tx2])   
    #matrizcG2[0] -> caracts gerais, matrizcG[1] -> especif tecnicas 
    matrizcG.append(matrizc)
 rt2.append(rt)
 rt2.append(matrizcG)
 return rt2

matriz_prod=[]
 
def parse_page(data_Res,file,orig_url,ky1,tot_prod):
 global start
 global matriz_prod
 data_Res=data_Res.replace('<strong>',' ')
 data_Res=data_Res.replace('</strong>',' ')
 data_Res=data_Res.replace('\n',' ')
 data_Res=data_Res.replace('&lt;strong>',' ')
 data_Res=data_Res.replace('&lt;/strong>',' ')
 data_Res=data_Res.replace('&lt;strong&lt;',' ')
 data_Res=data_Res.replace('&lt;/strong&lt;',' ')
 data_Res=data_Res.replace('<table>',' <table class =\"ficha-tecnica\"  >')
 # 
 soup = BeautifulSoup.BeautifulSoup(data_Res)
 #
 metas=parse_metas(soup)
 #
 cats=[]
 infos=[]
 tab_Caracts=[]
 tab_tecnica=[]
 preco=''
 try:
  cats=metas[0]
  infos=metas[1]
  try:
   tab_Caracts=metas[2][0] 
  except Exception,e:
   tab_Caracts=[]
   print 'Error(1):',e
   print 'url:',orig_url
 except Exception,e:
   print 'Error(geral):',e
   print 'url:',orig_url
   return
  #============
 #print infos
 # traduzir pra strem texto as informacoes acima
 info_prod=''
 for ct in (cats):
   fr=False
   d = ct[0]
   if info_prod == '':
    info_prod+=' categoria defs '
   elif info_prod != '':
     info_prod+=','
   if d == 'Moda, Calçados e Acessórios':
    info_prod+=' '+'Moda'+','+'Acessórios de moda' 
   else: 
    info_prod+=' '+d 
 if len(cats) > 0 :   
   info_prod+='. \n   '
 # apenas o ultimo item == descricao. os demais serao adicionados na tab diretamente  
 t_url=''
 t_title=''
 t_description=''
 t_image=''
 preco=''
 if len(infos) > 0: 
  cnd=0
  for i in infos:
    title=i[0]
    value=i[1]
    if title == '##image':
     t_image=i[1]
     continue
    if title == 'descricao':
     t_title=value
    else: 
     info_prod+='definicao defs '
     info_prod+=(title+' = '+value)
     info_prod+='. \n  ' 
    cnd+=1 
 #==========
 if len(tab_Caracts) > 0 : 
  for i in tab_Caracts:
   title=i[0]
   value=i[1]
   if title == 'descricao':
     t_title=value
   else:    
    info_prod+='definicao defs '
    info_prod+=(title+' = '+value)
    info_prod+='. \n ' 
 #==========
 if len(tab_tecnica) > 0 : 
  for i in tab_tecnica:
   title=i[0]
   value=i[1]
   info_prod+='definicao defs '
   info_prod+=(title+' = '+value)
   info_prod+='. \n ' 
 #=====================================
 #=====================================
 #=====================================
 #=====================================
 #file.write(str(info_prod))
 #return
 #
 try:
  #print 'post url short:',rturl
  c2=''
  try:
   rg=tab2.get(ky1)
   c2=umisc.trim(rg['lomadee_url'])
  except:
   c2=''
   pass
  #
  #msg_id=str(start+tot_prod)
  msg_id=ky1.encode('hex')
  url_lomad=c2
  t_title=t_title.replace('!',' ')
  t_title=t_title.replace('.',' ')
  t_title=t_title.strip('\n')
  t_title=t_title.strip('\r')
  t_title=t_title.strip('\t')
  
  if c2 == '':
   matriz_prod.append([msg_id,orig_url,ky1])
  wb2.insert((msg_id),{'url':orig_url,'pg':(info_prod),'lomadee_url':url_lomad,'termo':'product','usr':'index','purpose':'index','processed':'N','url_icon':'','url_picture':'','id_usr':'','name_usr':'','story':'','title':t_title,'doc_id':msg_id,'tp':'P','tps':'P','indexed':'N','id':msg_id,'_id':msg_id,\
  't_url':t_url,'t_title':t_title,'t_description':t_description,'t_image':t_image,"preco":preco,"prod":ky1})
 except Exception,errs:
  log.exception("(web_cache)" )
  rg=tab2.get(ky1)
  rg['INDEXED']='E' # fecha o produto indexado como error
  tab2.insert(ky1,rg)
 #===================================
 rg=tab2.get(ky1)
 rg['INDEXED']='S' # fecha o produto indexado
 tab2.insert(ky1,rg)

def lomadizar_urls():
 #url_lomad=ult_rturl['link_publish']
 orig_url=[]
 for [idprod,url,hi1] in matriz_prod:
  orig_url.append(url)
 #================= 
 lk=lomadeezar_links(orig_url)
 ult_rturl=None
 #print 'lomaddezar links:',len(lk)
 indlk=-1
 for rturl in lk:
   indlk+=1
   print 'gerate link:',indlk
   try:
    url_loma=rturl['redirectLink']
    _id=rturl['id']
   except:
     print 'ERROR:retorno.lomadee:',rturl
     continue
   shorted=short_url(url_loma)
   link_publish=shorted 
   ult_rturl=rturl
   print 'gerate link .finizhed :',indlk
   #==================================   
   [prod,url,ky1]=matriz_prod[int(_id)-1]
   rgcs=tab2.get(ky1)
   rgcs['lomadee_url']=link_publish
   tab2.insert(ky1,rgcs)
 
#========================================= teste
''' 
url='http://www.submarino.com.br/produto/117167963/sandalia-anabela-lilly-s-closet-cristais'


query=url
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.2) Gecko/20090729 Firefox/3.5.2 GTB5')]
data_Res = opener.open(query, '' ).read()
file=None
file = open("c:\\compartilhado\\cmp\\cc2.txt", "w")
ky=url
parse_page(data_Res,file,query,ky)
file.close()
'''

#==================================================================================================================================================


#========================================= quente
#============
def clear_dt(): 
 all_product=0
 rg=tab2.get_range()
 for ky,col in rg:
     col['INDEXED']='N' 
     #col['lomadee_url']=''
     tab2.insert(ky,col)
     all_product+=1
 #========== 
 print 'total products:',all_product


lenarg=len(sys.argv)

clearall='N'

if lenarg > 1: 
 clearall=sys.argv[1]

if clearall == 'S':
 wb2.truncate()
 clear_dt()

tot_prod=0
 
while True:
 cl4 = index.create_index_expression(column_name='INDEXED', value='N')
 clausec = index.create_index_clause([cl4],count=50)
 rg=tab2.get_indexed_slices(clausec)  
 #
 matriz_prod=[]
 # 
 cnt=0
 for ky,col in rg:
  url=ky
  cnt+=1
  tot_prod+=1
  print 'parse:',cnt,',total:',tot_prod  
  query=url
  opener = urllib2.build_opener()
  opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.2) Gecko/20090729 Firefox/3.5.2 GTB5')]
  #
  try:
   data_Res = opener.open(query, '' ).read()
  except:
   continue
  file=None
  #file = open("c:\\compartilhado\\cmp\\cc2.txt", "w")
  parse_page(data_Res,file,query,ky,tot_prod)
  #file.close()
  if cnt > 50: break;
  
 if len(matriz_prod) > 0: 
  lomadizar_urls()
#==================================================================================================================================================
