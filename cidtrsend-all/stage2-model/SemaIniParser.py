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
import umisc

import umisc
import Identify

import mdLayout
import mdER
import mdNeural


# obs : extrair informacoes -> preview de informacoes->pagina para exibir o resultado (href), titulo ou foco principal como result, classificacao como categoria --> para busca web realtime(busca na ontologia semanti_objects2 ,nao clipping

conn= None
conn4=None
conn3=None


 
 
   
def get_layouts(usr,purpose): 
 import mdER3
 print 'Get-layout-purpose:',purpose
 p =mdER3.get_LayoutsFZ(usr,purpose)
 return p   


def get_layouts2(usr,purpose): 
 import mdER3
 p =mdER3.get_LayoutsFZ2(usr,purpose)
 return p   


class thread_cntl:
 def __init__(self):
  self.finished=False
 
   
def entry_process(data_parse,usuario,purpose): 
 rets=[] 
 t_threads=[]
 t_threads.append(thread_cntl()) 
 onto_basis2=[]
 ontos=get_layouts(usuario,purpose)
 for onto_basisk in ontos:
     l2=Identify.prepare_layout(usuario,onto_basisk)
     onto_basis2.append(l2)
     
 onto_basis22=[]
 ontos2=get_layouts2(usuario,purpose)
 for onto_basisk in ontos2:
     l2=Identify.prepare_layout(usuario,onto_basisk)
     onto_basis22.append(l2)
 
 
 onto = Identify.pre_process_data2(onto_basis2,onto_basis22,data_parse,purpose,id,t_threads[len(t_threads)-1],[])
 

 for s in onto:
  rets.append(s)

 return rets
 
 
  
def trans(unic):
 ret_latin=''
 for s in unic:  
    ret_latin+=chr(ord(s))   
 return ret_latin
  
def entry(data,usr,purpose):
 data2=urllib.unquote(data)
 data=trans(data2)
 return entry_process(data,usr,purpose)   











 
 
 
 