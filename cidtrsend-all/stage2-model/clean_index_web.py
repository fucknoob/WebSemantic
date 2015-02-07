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
     
     

   
def clean_deps(usr):
  connidx1= MySQLdb.connect(host='dbmy0020.whservidor.com', user='mdnetsearc' , passwd='acc159753', db='mdnetsearc')
  connidx2= MySQLdb.connect(host='dbmy0031.whservidor.com', user='esyns1' , passwd='acc159753', db='esyns1')
  connidx3= MySQLdb.connect(host='dbmy0021.whservidor.com', user='mdnetsocia' , passwd='acc159753', db='mdnetsocia')
  #=
  cursordel1=connidx1.cursor ()
  cursordel2=connidx2.cursor ()
  cursordel3=connidx3.cursor ()
  # apagar urlinfo sem body
  sql1="DROP TEMPORARY TABLE IF EXISTS temp_cur1 "   
  cursordel1.execute(sql1)
  cursordel2.execute(sql1)
  cursordel3.execute(sql1)

  sql1="CREATE TEMPORARY TABLE temp_cur1 AS SELECT url_id FROM `urlinfo` WHERE sname like '%body%' "
  cursordel1.execute(sql1)
  cursordel2.execute(sql1)
  cursordel3.execute(sql1)
  
  sql1="delete from urlinfo where url_id not in ( SELECT url_id FROM temp_cur1 ) " 
  cursordel1.execute(sql1)
  cursordel2.execute(sql1)
  cursordel3.execute(sql1)

  


if True:
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
 #usrs=get_dist_usr() 
 #for us in usrs:
 #  clean_deps  (us)
 #time.sleep(10)


 
 
