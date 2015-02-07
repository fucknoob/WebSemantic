# coding: latin-1



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
import MySQLdb
import umisc

import Identify 


def clear_finizhed(usr,conn):
   cursor = conn.cursor ()
   cursor.execute ("delete from status_index_doc  where USERNAME = %s  and progress >=1 ",(usr))

def get_sum_stt(usr,conn):
   clear_finizhed(usr,conn)
   progress=0
   docid=0
   cursor = conn.cursor ()
   cursor.execute ("SELECT progress,DOCID from status_index_doc  where USERNAME = %s  order by i desc ",(usr))
   resultSet = cursor.fetchall()
   for results in resultSet:
      progress=results[0]
      docid=results[1]
      break
   return [progress,docid]


def  ret_lines_status(usr):
   rt=[]
   conn= MySQLdb.connect(host='dbmy0032.whservidor.com', user='mindnet_2' , passwd='acc159753', db='mindnet_2')
   cursor = conn.cursor ()
   cursor.execute ("SELECT cast( sum(progress) as char(20)),msg from status_index where USERNAME = %s and progress is not null ",(usr))
   resultSet = cursor.fetchall()
   for results in resultSet:
      i=results[0]
      d=results[1]
      if d == 'OK-FINAL3' or d == 'OK-FINAL2':
       i = d
       conn.close()
       if i == None: i=''
       return [i,'']
      sums=get_sum_stt(usr,conn)
      [progress,docid]=sums
      linha='DOC:'+str(docid)+' '+str(progress*100)+'%'
      conn.close()
      if i == None: i=''
      return [i,linha]
   return ['','']
   conn.close()

def  ret_usr(sessao):
   conn= MySQLdb.connect(host='dbmy0023.whservidor.com', user='mindnet' , passwd='acc159753', db='mindnet')
   cursor = conn.cursor ()
   cursor.execute ("SELECT USERNAME from usuarios where SESSAO= %s ",(sessao))
   resultSet = cursor.fetchall()
   for results in resultSet:
      i=results[0] 
      conn.close()
      return i
   conn.close()

def entry(req,logid):
 usr=ret_usr(logid)
 [ln,ln2]=ret_lines_status(usr)
 #==
 if ln2 == '' :
   return ln
 return (ln)+'|'+ln2
