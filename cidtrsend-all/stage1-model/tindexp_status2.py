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


def get_count_stt(usr):
   Ar=False
   conn= MySQLdb.connect(host='dbmy0032.whservidor.com', user='mindnet_2' , passwd='acc159753', db='mindnet_2')
   cursor = conn.cursor ()
   cursor.execute ("SELECT * from status_index_doc  where USERNAME = %s  LIMIT 0,5 ",(usr))
   resultSet = cursor.fetchall()
   for results in resultSet:
      Ar=True
   conn.close()
   return Ar

def  ret_lines_status(usr):
   if get_count_stt(usr):
    return 'OK-FINAL'
   rt=[]
   conn= MySQLdb.connect(host='dbmy0032.whservidor.com', user='mindnet_2' , passwd='acc159753', db='mindnet_2')
   cursor = conn.cursor ()
   cursor.execute ("SELECT cast( sum(progress) as char(20)),msg from status_index  where USERNAME = %s  order by i desc",(usr))
   resultSet = cursor.fetchall()
   for results in resultSet:
      i=results[0]
      d=results[1]
      if d == 'OK-FINAL' or d == 'OK-FINAL2' or d == 'OK-FINAL3' :
       i = d
      conn.close()
      return i
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
 ln=ret_lines_status(usr)
 #==
 return ln
