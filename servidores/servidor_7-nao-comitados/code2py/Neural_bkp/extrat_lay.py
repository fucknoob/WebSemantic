#coding: latin-1

''' inicializa o ambiente para captura de informacoes do clipping  '''

import MySQLdb
import Identify 
import mdNeural


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
import mdLayout
import mdER
import mdNeural
import mutex

import gc

import logging
from StringIO import StringIO
import datetime

logging.basicConfig(level=logging.DEBUG)
logs = logging.getLogger('indexerUSR')


ch  = logging.StreamHandler()
lbuffer = StringIO()
logHandler = logging.StreamHandler(lbuffer)

logs.addHandler(logHandler) 
logs.addHandler(ch) 



conn= MySQLdb.connect(host='dbmy0023.whservidor.com', user='mindnet' , passwd='acc159753', db='mindnet')
connTrace= MySQLdb.connect(host='dbmy0032.whservidor.com', user='mindnet_2' , passwd='acc159753', db='mindnet_2')
conn4=MySQLdb.connect(host='dbmy0050.whservidor.com', user='mindnet_4' , passwd='acc159753', db='mindnet_4') 
conn3= MySQLdb.connect(host='dbmy0035.whservidor.com', user='mindnet_3' , passwd='acc159753', db='mindnet_3') 
conn5= MySQLdb.connect(host='dbmy0039.whservidor.com', user='mindnet_5' , passwd='acc159753', db='mindnet_5') 

def config_conns(conn_):
 cursor=conn_.cursor()
 cursor.execute('SET SESSION wait_timeout = 90000')

config_conns(conn) 
config_conns(connTrace) 
config_conns(conn4) 
config_conns(conn3) 
config_conns(conn5) 
 

cursorTrace = connTrace.cursor ()

mdLayout.conn=conn
mdER.conn=conn
mdER.conn3=conn3
mdER.conn4=conn4

mdNeural.conn=conn
mdNeural.conn3=conn3
mdNeural.conn4=conn4

def clean_Trace(usr):
   cursorTrace.execute ("delete from status_index where USERNAME = %s  ",(usr))
   conn.commit()

def finish_Trace(usr):
   cursorTrace.execute ("insert into status_index(USERNAME,MSG) values ( %s , 'OK-FINAL' ) ",(usr))
   
 
mtx=mutex.mutex()
 
def traceQ(progress,usr):   
   if mtx.testandset():
    cursorTrace.execute ("insert into status_index(USERNAME,MSG,progress) values ( %s , '', %s ) ",(usr,progress))
    print 'TraceQ:===================='
    print progress
    print '==========================='
    mtx.unlock()
    return True
   return False 


def mount_node(term,id,purpose): 
 l=Identify.prepare_layout(id,purpose)
 allp=[]
 onto=Identify.prepare_data_by_ask(l, term,id,purpose,allp )
 return [onto,allp]

 
 
entry_doc =[]
 

 
def k1():
 usr='igor.moraes' 
 fh = open('c:\\compartilhado\\cmp\\k22.txt', "w")
 def clean_s(strc):
 
   strc=strc.replace('<subsign>','-')
   strc=strc.replace('<addsign>','+')
   strc=strc.replace('<divsign>','/')
   strc=strc.replace('<mulsign>','*')

   strc=strc.replace('<cite>','')
   strc=strc.replace('<em>','')
   strc=strc.replace('</em>','')
   strc=strc.replace('</cite>','')
   strc=strc.replace('<strong>','')
   strc=strc.replace('<string>','')
   strc=strc.replace('</string>','')
   strc=strc.replace('</strong>','')
   strc=strc.replace('<span style=\"text-decoration: underline;\">','')
   strc=strc.replace('<span','')
   strc=strc.replace('id=\"\">','')
   strc=strc.replace('</span>','')
   strc=strc.replace('<br>','\n')
   strc=strc.replace('<s>','')
   strc=strc.replace('</s>','')
   strc=strc.replace('</u>','')
   strc=strc.replace('<u>','')
   strc=strc.replace('<i>','')
   strc=strc.replace('</i>','')
   strc=strc.replace('<space>',' ')
   strc=strc.replace('<b>',' ')
   strc=strc.replace('<b>','')
   strc=strc.replace('</b>','')
   
   
   
   
   
   return strc
 
 #chamar os codigos 
 if True:
  cursor = conn.cursor ()
  cursor.execute ("select CODE from DATA_BEHAVIOUR_CODE where    USERNAME='"+usr+"' order by i") 
  resultSet = cursor.fetchall()
  for results in resultSet:
    o=clean_s(results[0])
    code=(o)
    fh.write(code)
    #================================== 
 #===================
 fh.close()
 
k1()