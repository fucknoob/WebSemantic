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


import socket
   
def run_cmd(cmd):
 client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 client_socket.connect(("localhost", 5000))   
 client_socket.send(cmd)
   
   
def entry(req,logid):
 usr=ret_usr(logid)
 #cmd1='python /home/mindnet/public_html/Neural/SemaIndexerUsr.py ' + ' "'+usr+'" >/dev/null & ' 
 #os.system(cmd1)
 try:
  run_cmd(usr)
 except : pass 
 #============================
 return 'CmdOK'
