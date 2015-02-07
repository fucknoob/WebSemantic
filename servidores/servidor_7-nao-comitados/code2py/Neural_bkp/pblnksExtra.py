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

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('pblnksExtra')


ch  = logging.StreamHandler ()
lbuffer = StringIO ()
logHandler = logging.StreamHandler(lbuffer)

log.addHandler(logHandler) 
log.addHandler(ch) 



pool2 = ConnectionPool('MINDNET', ['localhost:9160'],timeout=10)
tab2 = pycassa.ColumnFamily(pool2, 'cache_products')
wb2 = pycassa.ColumnFamily(pool2, 'web_cache3') # lugar para indexar 
 
 
 
def short_url(urllong):
 return bitly.short_url(urllong)
 
def lomadeezar_links(links_tw):
 areturn=[]
 lnk=[]
 ind=1
 for l in links_tw:
   #l=urllib.quote(l)
   lnk.append(['link'+str(ind),l])
   ind+=1
 url='http://ws.buscape.com/service/createLinks/lomadee/564771466d477a4458664d3d/?'
 #url='http://sandbox.buscape.com/service/createLinks/lomadee/564771466d477a4458664d3d/?' 
 args = {}    
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
   args={}
   for n3 in n2:
    n4=n3.getElementsByTagName('lomadeeLink')
    for n5 in n4:
     for n6 in n5.getElementsByTagName('originalLink'):
      args['originalLink']=n6.firstChild.data
     for n7 in n5.getElementsByTagName('redirectLink'): 
      args['redirectLink']= n7.firstChild.data
     for n8 in n5.getElementsByTagName('code'): 
      args['code']= n8.firstChild.data
     for n9 in n5.getElementsByTagName('id'): 
      args['id']= n9.firstChild.data
     areturn.append(args)
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
 def parse_item(dv):
  t1=dv[0]
  return [t1['name'].replace(':','_').encode('latin-1', 'ignore'),t1['content'].encode('latin-1', 'ignore')]
 def parse_q(soup,name):
  divc2=soup.findAll('meta',attrs={"name":name})
  ks= parse_item(divc2)
  return ks
 rt=[] 
 #rt.append( parse_q(soup,"twitter:card") )
 rt.append( parse_q(soup,"twitter:url") )
 #rt.append( parse_q(soup,"twitter:site") )
 #rt.append( parse_q(soup,"twitter:creator") )
 rt.append( parse_q(soup,"twitter:title") )
 rt.append( parse_q(soup,"twitter:description") )
 rt.append( parse_q(soup,"twitter:image") )
 rt.append( [parse_q(soup,"twitter:label1")[1],parse_q(soup,"twitter:data1")[1]] ) 
 rt.append( [parse_q(soup,"twitter:label2")[1],parse_q(soup,"twitter:data2")[1]] ) 
 # parse html itens 
 descr_P=''.encode('latin-1','ignore')
 descr_All=soup.findAll("div",id="descricao")
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
  

 # parse categoria
 categ=soup.findAll("div",attrs={'class':'wp'})
 caracts_cateh=[]
 cats=[]
 for ittb in  categ:
   lnc=len(ittb.contents)
   matrizc=[]
   atct=False
   for elm in ittb.contents:
    if getattr(elm, 'name', None) == 'a':
       tx=''
       if type(elm).__name__ == 'Tag':
        tx=elm.getText(' ').encode('latin-1', 'ignore')
       if type(elm).__name__ == 'NavigableString':
        tx=elm.encode('latin-1', 'ignore')
       tx=tx.replace(' - ','\n') 
       tx=umisc.trim(tx)
       if tx == 'Moda':
         atct=True
       if atct:         
         matrizc.append(tx)
   if len(matrizc) > 0:
    if 'Moda' in matrizc: 
     cats=(matrizc)   
 if len(cats)>0:
    caracts_cateh.append(cats)
    cats=[]
 # parse caracts table
 rt2=[] 
 rt2.append(caracts_cateh) 
 matrizcG=[]
 tbs_ln=soup.findAll("div",attrs={'class':'wrp'})
 for ittb in  tbs_ln:
   lnc=len(ittb.contents)
   matrizc=[]
   for elm in ittb.contents:
    if getattr(elm, 'name', None) == 'dl':
     tx1=''
     tx2=''
     for elm2 in elm.contents:
        if getattr(elm2, 'name', None) == 'dt':
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
        if getattr(elm2, 'name', None) == 'dd':
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

 
def parse_page(data_Res,file,orig_url,ky1):
 data_Res=data_Res.replace('<strong>',' ')
 data_Res=data_Res.replace('</strong>',' ')
 data_Res=data_Res.replace('\n',' ')
 data_Res=data_Res.replace('&lt;strong>',' ')
 data_Res=data_Res.replace('&lt;/strong>',' ')
 data_Res=data_Res.replace('&lt;strong&lt;',' ')
 data_Res=data_Res.replace('&lt;/strong&lt;',' ')
 
 soup = BeautifulSoup.BeautifulSoup(data_Res)
 #
 metas=parse_metas(soup)
 #
 #metas[0]->categoria-> ex.moda>moda masculina>bermunda ...
 #metas[1]->info twitter e descricao do produto(descr principal )
 #metas[2]->metas[1][0] -> tabela de caracts , metas[1][1] -> defs tecnicas 
 cats=[]
 infos=[]
 tab_Caracts=[]
 tab_tecnica=[]
 try:
  cats=metas[0]
  infos=metas[1]
  try:
   tab_Caracts=metas[2][0] 
  except Exception,e:
   tab_Caracts=[]
   print 'Error(1):',e
   print 'url:',orig_url
  try: 
   tab_tecnica=metas[2][1] 
  except Exception,e:
   tab_tecnica=[]
   print 'Error(2):',e
   print 'url:',orig_url  
 except Exception,e:
   print 'Error(geral):',e
   print 'url:',orig_url
   return
   
 #print infos
 # traduzir pra strem texto as informacoes acima
 info_prod=''
 for ct in (cats):
  info_prod='categoria defs '
  fr=False
  for d in ct:  
   if fr:
    info_prod+=','+d 
   else:
    info_prod+=' '+d 
   fr=True
  info_prod+='.\n'
 # apenas o ultimo item == descricao. os demais serao adicionados na tab diretamente  
 t_url=''
 t_title=''
 t_description=''
 t_image=''
 preco=''
 if len(infos) > 0: 
  cnd=0
  for i in infos:
   if cnd == 0:
    t_url=i[1]
   elif cnd == 1:
    t_title=i[1]
   elif cnd == 2:
    t_description=i[1]
   elif cnd == 3:
    t_image=i[1]
   elif cnd == 4:
    pass
   elif cnd == 5:
    preco=i[1]
   else: 
    info_prod+='definicao defs '
    title=i[0]
    value=i[1]
    info_prod+=(title+' = '+value)
    info_prod+='.\n' 
   cnd+=1 
 #==========
 if len(tab_Caracts) > 0 : 
  for i in tab_Caracts:
   info_prod+='definicao defs '
   title=i[0]
   value=i[1]
   info_prod+=(title+' = '+value)
   info_prod+='.\n' 
 #==========
 if len(tab_tecnica) > 0 : 
  for i in tab_tecnica:
   info_prod+='definicao defs '
   title=i[0]
   value=i[1]
   info_prod+=(title+' = '+value)
   info_prod+='.\n' 
 #=====================================
 #=====================================
 #=====================================
 #=====================================
 #file.write(str(info_prod))
 #return
 #print info_prod  
 #
 lk=lomadeezar_links([orig_url])
 ult_rturl=None
 for rturl in lk:
   shorted=short_url(rturl['redirectLink'])
   rturl['link_publish']=shorted 
   ult_rturl=rturl
 
 #print lk
 #print info_prod
 # gravar lk e info_prod no banco de dados, para analize de caracts e url de publicacao
 #
 try:
  #print 'post url short:',rturl
  msg_id=ult_rturl['link_publish']
  wb2.insert(msg_id,{'url':orig_url,'pg':(info_prod),'lomadee_url':msg_id,'termo':'product','usr':'index','purpose':'index','processed':'N','url_icon':'','url_picture':'','id_usr':'','name_usr':'','story':'','title':'','doc_id':msg_id,'tp':'P','tps':'P','indexed':'N','id':msg_id,'_id':msg_id,\
  't_url':t_url,'t_title':t_title,'t_description':t_description,'t_image':t_image,"preco":preco})
 except Exception,errs:
  log.exception("(web_cache)" )
  rg=tab2.get(ky1)
  rg['INDEXED']='E' # fecha o produto indexado como error
  tab2.insert(ky1,rg)
 #===================================
 rg=tab2.get(ky1)
 rg['INDEXED']='S' # fecha o produto indexado
 tab2.insert(ky1,rg)

 

''' 
url='http://www.extra.com.br/Moda/RoupasMasculinas/CamisasPolo/Camisa-Polo-Pique-Masculina-The-Great-One-Zebra-Azul-Provence-2472220.html'
#url='http://www.extra.com.br/Moda/RoupasFemininas/Blusas/Kit-com-2-Camisetas-Feminina-Regata-Hanes-Preta-Mescla-2181075.html'


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


while True:
 cl4 = index.create_index_expression(column_name='INDEXED', value='N')
 clausec = index.create_index_clause([cl4],count=50)
 rg=tab2.get_indexed_slices(clausec)  
 #
 cnt=0
 for ky,col in rg:
  url=ky
  cnt+=1
  print 'parse:',cnt
  query=url
  opener = urllib2.build_opener()
  opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.2) Gecko/20090729 Firefox/3.5.2 GTB5')]
  #
  data_Res = opener.open(query, '' ).read()
  file=None
  #file = open("c:\\compartilhado\\cmp\\cc2.txt", "w")
  parse_page(data_Res,file,query,ky)
  #file.close()
  if cnt > 50: break;

 
