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

 

def demove_task_finish(usr):
 sql='delete from INBOX_MSG  where USERNAME=?'
 session.sqlX (sql,([usr]))
 session.commit()
 return "[OK]"

 
 
def process_mx(usr_n):
 #
 T=demove_task_finish(usr_n)
 # 
 return 'OK-FINAL-'+T
 
def entry(req,logid):
  usr=logid
  if usr != None:
   return process_mx(usr)
  return ''

 
 