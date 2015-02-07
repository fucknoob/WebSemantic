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

import umisc
import Identify

import mdLayout
import mdER
import mdNeural


# obs : extrair informacoes -> preview de informacoes->pagina para exibir o resultado (href), titulo ou foco principal como result, classificacao como categoria --> para busca web realtime(busca na ontologia semanti_objects2 ,nao clipping

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

def clean_Trace(usr):
   cursorTrace.execute ("delete from status_index where USERNAME = %s  ",(usr))
   
def finish_Trace(usr):
   cursorTrace.execute ("insert into status_index(USERNAME,MSG) values ( %s , 'OK-FINAL' ) ",(usr))

def traceQ(progress,usr,pg_numer,job,address,msg ):   
   linha=str(progress)+'|'+ msg+ ',Pg:'+str(pg_numer)+',Process:'+str(job)+',Address:'+address
   cursorTrace.execute ("insert into status_index(USERNAME,MSG) values ( %s , %s )  ",(usr,linha))
   print 'TraceQ:===================='
   print linha
   print '==========================='


   
def entry_process(param,data_parse,usr):
 
 layouts_f=get_layouts(usr,'simple-search')
 layouts_f2=get_layouts2(usr,'simple-search')
 
 
 rets=[]
 str_ret=[]
 
 l=Identify.prepare_layout(usr,'simple-search')
 l2=Identify.prepare_layout(usr,'simple-search')
 onto=Identify.prepare_data_by_ask(l, param,usr,'simple-search',[] )
 
 
 for dta in data_parse:
  ir=Identify.process_data(l2,dta,onto,'simple-search',usr) 
  if ir[0] == None: continue
  for topico in ir[0].topicos:
   if len(topico.dt) > 0 :
    it=topico.dt
    its=[]
    for p in topico.sinapses:
      its.append([p.opcode,p.nr.dt])
    rets.append([it,its])
      
 for tp in rets:   
    if 'identificador' in tp[0] :
     c2= tp[1]
     for tp2 in c2:
      for dt in tp2[1]:
       str_ret.append(dt)
 #========================================      
 sret='%'
 for s in str_ret:
  sret+=(s+'%')
 #================== 
 if sret=='%':
   sret+=(param+'%')
   
 return sret
  
def trans(unic):
 ret_latin=''
 for s in unic:  
    ret_latin+=chr(ord(s))   
 return ret_latin
  
def entry(req,data,usr):
 #data2=urllib2.quote(data)
 #data2=urllib.unquote(data).decode('utf-8')
 data2=urllib.unquote(data)
 data=trans(data2)
 return entry_process(data,[data],usr)   











 
 
 
 