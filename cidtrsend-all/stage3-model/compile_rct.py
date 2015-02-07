from mod_python import apache

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
import mdER
import MySQLdb
import umisc

import mdLayout
import mdER
import mdNeural


def ret_usr(sessao):
 sql1="SELECT USERNAME from usuarios where SESSAO='"+sessao+"' "
 conn= MySQLdb.connect(host='dbmy0023.whservidor.com', user='mindnet' , passwd='acc159753', db='mindnet')
 cursor = conn.cursor ()
 cursor.execute (sql1)
 resultSet = cursor.fetchall()
 rs=[]
 for results in resultSet:
  code=results[0]
  if code != '' : 
   conn.close()
   return code
 #========
 conn.close()
 return ''

conn= MySQLdb.connect(host='dbmy0023.whservidor.com', user='mindnet' , passwd='acc159753', db='mindnet')
connTrace= MySQLdb.connect(host='dbmy0032.whservidor.com', user='mindnet_2' , passwd='acc159753', db='mindnet_2')
conn4=MySQLdb.connect(host='dbmy0050.whservidor.com', user='mindnet_4' , passwd='acc159753', db='mindnet_4') 
conn3= MySQLdb.connect(host='dbmy0035.whservidor.com', user='mindnet_3' , passwd='acc159753', db='mindnet_3') 

def config_conns(conn_):
 cursor=conn_.cursor()
 cursor.execute('SET SESSION wait_timeout = 90000')

config_conns(conn) 
config_conns(connTrace) 
config_conns(conn4) 
config_conns(conn3) 
 

cursorTrace = connTrace.cursor ()

mdLayout.conn=conn
mdER.conn=conn
mdER.conn3=conn3
mdER.conn4=conn4

mdNeural.conn=conn
mdNeural.conn3=conn3
mdNeural.conn4=conn4


def entry(req,usr):
 usr2=ret_usr(usr)
 mdER.compile_rct(usr2)
 
 
 
 
 
 