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

def  ret_lines_status(usr): 
   rt=[]
   conn= MySQLdb.connect(host='dbmy0032.whservidor.com', user='mindnet_2' , passwd='acc159753', db='mindnet_2')
   cursor = conn.cursor ()
   cursor.execute ("SELECT msg from status_index3  where USERNAME = %s  order by i desc",(usr))
   resultSet = cursor.fetchall()
   for results in resultSet:
      d=results[0]
      if d == 'OK-FINAL'   :
       i = d
       conn.close()
       return i   
   conn.close()
   return 'CmSD'

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
