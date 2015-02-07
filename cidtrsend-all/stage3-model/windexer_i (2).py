#coding: latin-1

''' inicializa o ambiente para captura de informacoes do clipping  '''

import MySQLdb
 

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
import umisc
 
import subprocess
import string

 
conn= MySQLdb.connect(host='dbmy0023.whservidor.com', user='mindnet' , passwd='acc159753', db='mindnet')
 
 
def config_conns(conn_):
 cursor=conn_.cursor()
 cursor.execute('SET SESSION wait_timeout = 90000')

config_conns(conn) 



def prepare_search(dts):
 
 rets=[]
 if True :
  qry=''
  for d in dts:
   qry+=d+' '
  query=urllib.quote(qry)
  url_q='http://www.mind-net.com/Neural/request_md3.py/entry?query='+query+'&t=web'
  opener = urllib2.build_opener()
  data_Res = opener.open(url_q, '' ).read()
  lines=[]
  cl=[]
  tmp='';
  kind=1
  for ds in data_Res:
   if ds == '|':
    if len(tmp) > 0 :
     cl.append(tmp)
     tmp=''
    lines.append(cl)
    cl=[]
   elif ds == '^':
    cl.append(tmp)
    tmp=''     
   else:
    tmp+=ds
  rets.append(lines) 
  #
 return rets


class thread_cntl:
 def __init__(self):
  self.finished=False

class Task_C:
 def __init__(self,Dt1=None,Dt2=None,Dt3=None,tp=None):
   self.dt1=Dt1
   self.dt2=Dt2
   self.dt3=Dt3
   self.Tp=tp
  

cursorpostp = conn.cursor ()
cursorpostl = conn.cursor ()

  

def post_links(endereco,termo,usr,purp):
 try:
   sql1="insert into WEB_CACHE_LINKS (URL,TERMO,PURPOSE,USR,PROCESSED) values(%s,%s,%s,%s,'N')"
   if umisc.trim(endereco) != '':
    cursorpostl.execute (sql1,(MySQLdb.escape_string(endereco),MySQLdb.escape_string(termo),purp,usr))
 except:
  pass

 
class thread_cntl:
 def __init__(self):
  self.finished=False

 
def run_cmd_s(d,th):
   try:
    os.system("/home/esyns1/public_html/dpsearch/sbin/indexer  ")
   except:
    pass
   th.finished=True
   
def get_langs(usr):
     sql1="select LABEL FROM knowledge_manager WHERE USERNAME =  %s  AND typ =4 and DT='language'  ORDER BY i "
     rt=[]
     cursor = conn.cursor ()
     cursor.execute (sql1,(usr)) #  
     resultSet = cursor.fetchall()
     for results in resultSet:
        username=results[0]
        rt.append(username)
     return rt
     
     
   
def clear_langs(usr,connidx1,connidx2,connidx3):
  cursordel1=connidx1.cursor ()
  cursordel2=connidx2.cursor ()
  cursordel3=connidx3.cursor ()
  
  strlangs='';
  for s in get_langs(usr):
   s1='\''+s+'\''
   if strlangs != '':
     strlangs+=','
   strlangs+=s1

  sql2="delete from url where rec_id in ( SELECT url_id FROM `urlinfo` WHERE sname like '%Content-Language%' and sval not in("+strlangs+")   ) " 
  cursordel1.execute(sql2)
  cursordel2.execute(sql2)
  cursordel3.execute(sql2)

  strlangs='';
  for s in get_langs(usr):
   s1='\\\''+s+'\\\''
   if strlangs != '':
     strlangs+=','
   strlangs+=s1

  sql1="call p30 ('"+strlangs+"')   " 
  print sql1
  cursordel1.execute(sql1)
  cursordel2.execute(sql1)
  cursordel3.execute(sql1)
   
   
def clean_deps():
   try:
    os.system("python /home/esyns1/public_html/Neural/clean_index_web.py  ")
   except:
    pass
  
   
def call_links():
  i=0
  ths=[]
  while i < 3:
   print 'Start indexer '+str(i)
   #proc = subprocess.Popen("/home/mindnet/public_html/dpsearch/sbin/indexer  ", shell=True,stdout=subprocess.PIPE)
   #proc = subprocess.Popen("/home/esyns1/public_html/dpsearch/sbin/indexer  ", shell=True,stdout=subprocess.PIPE)
   ths.append(thread_cntl())
   thread.start_new_thread(run_cmd_s,(1,ths[len(ths)-1] ) )
   time.sleep(10)
   i+=1

  ind_col=0
  while True:
   print 'wait for pages...',len(ths)-ind_col
   fnds_t=False
   ind_col=0
   for ths1 in ths:    
    if not ths1.finished:fnds_t=True
    if ths1.finished: ind_col+=1
   if fnds_t:
    time.sleep(10)
    continue
   else:
    break   
  #==
  clean_deps()

  
def process_termo(termo,usr,purp,start_c,path_j,layout):
 objs_search=[]
 purposes=[]
 purposes.append(purp)
   
 #==================================
 objs_search.append(termo)
 #==================================
 
 if len(objs_search) > 0 :
  def pg_open(addresss,th,pages,pgind,ind_emit,start_c,tp):
   print 'Start read page:',addresss
   try:
    for address in addresss:
        lines_doc=[]
        links_k2=[]
        if address != 'debug-url':
         #======================
         opener = urllib2.build_opener()
         address=urllib.quote(address)
         url='http://www.mind-net.com/get_Text.php?q='+address
         content = opener.open(url, '' ).read()
         tmpd=''
         for d in content:
          if d == '\n':
           tmpd=umisc.trim(tmpd)
           lines_doc.append(tmpd)
           tmpd=''
          else:
           tmpd+=d    
         #======================
         opener = urllib2.build_opener()         
         url='http://www.mind-net.com/get_links2.php?q='+address
         content = opener.open(url, '' ).read()
         tmpd=''
         for d in content:
          if d == '\n':
           tmpd=umisc.trim(tmpd)
           links_k2.append(tmpd)
           tmpd=''
          else:
           tmpd+=d    
         #============
         pages.append(Task_C(pg_add,lines_doc,links_k2,tp))
         print 'Get content for page:',pgind,' was finished.Len:',len(lines_doc),' links count:',len(links_k2)
         pgind+=1
        else:
         pass
         
    th.finished=True
   except Exception,er :
    print er,'................'
    th.finished=True
  #=====================================================  
  results_search=[]
  #=====================================================
  if 'url' in purposes:
   results_search = [[['url',objs_search[0]]]] #busca direta por url
  
  cind=0
  pages=[]
  kind=0
  print 'Init Collect...'
  #=====================================
  indres=0
  ths=[]
  ths2=[]
  #========================
  ind_emit=0
  tmp_pages=[]
  for res in results_search:
   indaddrs=0
   for addrs in res:
     tp=addrs[0]
     pg_add=addrs[1]
     ind_emit+=1
     if len(tmp_pages) >=5 :
      ths.append(thread_cntl())
      ic=ind_emit
      tmp_pages2=tmp_pages
      tmp_pages=[]
      thread.start_new_thread(pg_open,(tmp_pages2,ths[len(ths)-1],pages,kind,ic,start_c,tp) )
     else:
      tmp_pages.append(pg_add)      
   cind+=1
   indres+=1
  if len(tmp_pages) > 0 :
      ths.append(thread_cntl())
      ic=ind_emit
      tmp_pages2=tmp_pages
      tmp_pages=[]
      thread.start_new_thread(pg_open,(tmp_pages2,ths[len(ths)-1],pages,kind,ic,start_c,tp) )
  
  ind_col=0
  #============================= 
  while True:
   print 'wait for pages...',len(ths)-ind_col
   fnds_t=False
   ind_col=0
   for ths1 in ths:    
    if not ths1.finished:fnds_t=True
    if ths1.finished: ind_col+=1
   if fnds_t:
    time.sleep(10)
    continue
   else:
    break
 
  print 'Collect OK!!'
  cind2=0
  threads_fd=[]
  
  
  print 'Init Process pages:',len(pages)
  for pagina in pages:
   cind2+=1
   if pagina.dt1 == None: continue
   endereco=pagina.dt1
   lines_doc=pagina.dt2
   links=pagina.dt3
   tp=pagina.Tp
   if tp != None :
     if tp=='url':
       for ln in links:
        post_links(ln,endereco,usr,purp)
       continue    
   


def fecha_busca(termo,username): 
 #==
 sql1=" update knowledge_manager  set srched='S' where USERNAME = %s  and dt= %s "
 cursor = conn.cursor ()
 cursor.execute (sql1,( username,MySQLdb.escape_string(termo)))
 #==
 
def fecha_busca2(termo,username): 
 #==
 sql1=" delete from WEB_CACHE_LINKS  where USR = %s  and url= %s "
 cursor = conn.cursor ()
 cursor.execute (sql1,( username,MySQLdb.escape_string(termo)))
 #==

def limpa_resultados_anteriores(termo,username,purp): 
 #==
 sql1="delete from WEB_CACHE where TERMO= %s and USR=%s and PURPOSE= %s "
 cursor = conn.cursor ()
 cursor.execute (sql1,(MySQLdb.escape_string(termo),username,purp))
 #==

def abre_buscas():
 cursor = conn.cursor ()
 cursor.execute ("update knowledge_manager set srched='N' where typ=2   ")  
 #================
 cursor = conn.cursor ()
 cursor.execute ("delete from WEB_CACHE  ") 
 #================
 cursor = conn.cursor ()
 cursor.execute ("delete from WEB_CACHE_LINKS  ") 
 
def process_sentences(start_c): 
 cursor = conn.cursor ()
 cursor.execute ("SELECT USERNAME,DT,LAYOUT_ONTO,DEST FROM knowledge_manager  where typ=2 and srched='N' LIMIT 0 , 50 ") # 50 rows por vez
 resultSet = cursor.fetchall()
 for results in resultSet:
    username=results[0]
    termo=results[1] 
    layout=results[2] 
    dest=results[3] 
    #r1.append([username,termo,layout,dest])
    limpa_resultados_anteriores(termo,username,dest)
    process_termo(termo,username,dest,start_c,sys.argv[0],layout)
    #=== fecha os ja executados
    fecha_busca(termo,username)
    

def process_sentences2(start_c): 
 #========================    
 def get_dist_usr():
     rt=[]
     cursor = conn.cursor ()
     cursor.execute ("SELECT distinct USERNAME  FROM knowledge_manager  where typ=2    ") #  
     resultSet = cursor.fetchall()
     for results in resultSet:
        username=results[0]
        rt.append(username)
     return rt

 def get_dist_url():
     rt=[]
     cursor = conn.cursor ()
     cursor.execute ("SELECT distinct DT  FROM knowledge_manager  where typ=2 and dest='url'   ") #  
     resultSet = cursor.fetchall()
     for results in resultSet:
        username=results[0]
        rt.append(username)
     return rt

     
 usrs=get_dist_usr() 
 if True:
  url=[]
  users_l=[]
  for us in usrs:
     users_l2=get_langs(us)
     for l2 in users_l2:
       users_l.append(l2)
     cursor = conn.cursor ()
     cursor.execute ("SELECT  URL  FROM WEB_CACHE_LINKS  where USR=%s  ",MySQLdb.escape_string(us))  
     resultSet = cursor.fetchall()
     for results in resultSet:
        url.append(results[0]) 
 
  print 'Clean cache older'
  clean_deps()
  time.sleep(10)
  print 'Urls collecteds:',len(url)
  if len(url) > 0 :
      #==
      file = open("/home/esyns1/public_html/dpsearch/etc/indexer.conf2", "r")
      #file = open("/home/mindnet/public_html/dpsearch/etc/indexer.conf2", "r")
      oldtxt=file.read()
      #file = open("/home/mindnet/public_html/dpsearch/etc/indexer.conf", "w")
      file = open("/home/esyns1/public_html/dpsearch/etc/indexer.conf", "w")
      file.write(oldtxt+"\n")    
      #if len(users_l) > 0 :
      # file.write(" NoIndexIf Content-Language * \n")
      #for l in users_l:
      # file.write(" IndexIf Content-Language "+l+"* \n")
      
      if len(users_l) > 0 :
       file.write(" Disallow NoMatch * \n")       
      for l in users_l:
       file.write(" allow Match *"+l+"* \n")
      #====================================================
      for serv in get_dist_url():
       file.write('Server '+serv+"\n")
      #====================================================      
      for url1 in url:
       file.write('URL '+url1+"\n")
      file.close()
      #==   
      usrs=get_dist_usr() 
      call_links()

    
    
start_c=0

reindex=False

index_all_of=False #usando para indicar se vai indexar ou nao o web_cache_url

if len(sys.argv) > 1:     
 reindex= int(sys.argv[1]) >0
      
if len(sys.argv) > 2:     
 index_all_of= int(sys.argv[2]) >0
 
if reindex:
 abre_buscas() 
 
process_sentences(start_c)

if index_all_of:
 process_sentences2(start_c)
 i=1
 while i < 50000:
   try:
     clean_deps()
   except :pass
   try: 
     call_links()
   except: pass
   i+=1
   time.sleep(5*60)
else:
 def get_dist_usr():
     rt=[]
     cursor = conn.cursor ()
     cursor.execute ("SELECT distinct USERNAME  FROM knowledge_manager  where typ=2    ") #  
     resultSet = cursor.fetchall()
     for results in resultSet:
        username=results[0]
        rt.append(username)
     return rt
 print 'Clean cache older'
 clean_deps  ()
 time.sleep(10)
 i=0
 while i < 50000:
  call_links()
  i+=1
  time.sleep(5 * 60) # 05 minutos

 
 
