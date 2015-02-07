# coding: latin-1



import base64
import calendar
import os
import rfc822

import sys
sys.path.append('/Neural/mxdb')
sys.path.append('/Neural')
 

import tempfile
import textwrap
import time
import urllib
import urllib2
import urlparse
 
 
import maxdb 
 
 

   
user = 'MIND'
pwd = 'MIND'
dbname = 'mindnet'
host = 'localhost'
 
session = maxdb.connect (user, pwd, dbname, host)   


def marca_process_start(usr):
 sql='insert into usr_task(usr) values(?)'
 session.sqlX (sql,([usr]))
 session.commit()

def demove_task_finish(usr):
 sql='delete from usr_task where usr=?'
 session.sqlX (sql,([usr]))
 session.commit()

def verifica_usuario_pend(usr) :
 sql='select * from usr_task where usr=? '
 resultSet =session.sqlX (sql,([usr]))
 F=False
 for results in resultSet:  
   F=True 
 return F
 
def process_mx(usr_n,query):
 #
 s='Prepare\n'
 args=[usr_n,query,"simple-search-ask-aswer","1",query]
 import SemaIndexerStage3C 
 T=verifica_usuario_pend(usr_n)
 if not T:
  marca_process_start(usr_n)   
  try:
   s+='Execute\n'
   r2=SemaIndexerStage3C.entry(args)
   s+='Executed..\n'
   s+=r2
  except Exception,e: 
   s+='(Error:'+e.__str__()+')'
  demove_task_finish(usr_n)
  s+='|remove-task|'
 else:
  return ('ALL-RUN-'+s)
 # 
 #
 return 'OK-FINAL-'+s
 
def entry(req,logid,query):
  usr=logid
  if usr != None:
   return process_mx(usr,query)
  return ''

 
 