# coding: latin-1



import base64
import calendar
import os
import rfc822

import sys
sys.path.append('/Neural/mxdb')
 

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
 
def process_mx(usr_n):
 #
 #
 try:
  stmt = "SELECT MSG,SOURCE,REFERENCIAS from INBOX_MSG where USERNAME = \'"+usr_n+"\'  order by i desc "
  
  prepar = session.prepare (stmt)
  values = [0]
  result = prepar.execute (values)
 except maxdb.sql.SQLError,e: 
  msg=str(e.errorCode)+"["+e.message+"]"
  print( msg )
   
 
 row = result.next ()
 
 str_r=""
 
 while row:
  msg= row[0].read() 
  source= row[1]
  refs= row[2].read()
  lnk=( msg + '\2' + source + '\2' + refs + '\2' )
  lnk+= '\3'
  str_r+=  lnk
  row = result.next ()
 
 return (str_r)  
 
def entry(req,logid):
  #usr=ret_usr(logid)
  usr=logid
  if usr != None:
   return process_mx(usr)
  return ''

 
 