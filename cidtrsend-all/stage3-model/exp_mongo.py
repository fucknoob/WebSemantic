import os
import sys

import pycassa
from pycassa.pool import ConnectionPool
from pycassa import index
from pycassa.columnfamily import ColumnFamily

import pymongo

pool2 = ConnectionPool('MINDNET', ['91.205.172.85:9160'],timeout=500000)
fcb = pycassa.ColumnFamily(pool2, 'fcb_users') 
rest=fcb.get_range()

#MONGO_URL='mongodb://mind1:acc159753@ds031978.mongolab.com:31978/mind1'

url_1='mongodb://mdnet1_1:acc159753@ds035348.mongolab.com:35348/mdnet1_1'

url_2='mongodb://mdnet1_2:acc159753@ds035358.mongolab.com:35358/mdnet1_2'

url_3='mongodb://mdnet1_3:acc159753@ds035348.mongolab.com:35348/mdnet1_3' 

url_4='mongodb://mdnet1_4:acc159753@ds035348.mongolab.com:35348/mdnet1_4' 

url_5='mongodb://mdnet1_5:acc159753@ds035358.mongolab.com:35358/mdnet1_5' 


import socket 
import thread               
sr = socket.socket()          
hostr = socket.gethostname()  
portr = 12224
atu_reg='no.ref'
atu_reg2='-'

def serve_stats(dmu,dmu2):
 global atu_reg
 sr.bind((hostr, portr))        # Bind to the port
 sr.listen(20)                 # Now wait for client connection.
 while True:
   cr, addr = sr.accept()     # Establish connection with client.
   print 'Got connection from', addr
   msg = cr.recv(1024)
   #print addr, ' >> ', msg
   msg = str(atu_reg)+'|'+str(atu_reg2)
   cr.send(msg);
   
thread.start_new_thread(serve_stats,(0,0) )  

def process1():
 global atu_reg 
 global atu_reg2
 conn_mongo = pymongo.Connection(url_1)
 mongo_db = conn_mongo['mdnet1_1']
 fcb_m = mongo_db['fcb_users']
 indk1=1 
 index_cnts1=0
 for kl,cols in rest:
        #==============
        index_cnts1+=1
        id=cols['id']   
        indexed=cols['indexed']
        u_name=cols['u_name'] 
        user_name=cols['user_name']  
        if index_cnts1 % 1000 == 0 : 
          #print 'index_cnts1:',index_cnts1
          atu_reg='index_cnts1(1):'+str(index_cnts1)
        if indexed == 'N':        
          #print "id:",id,',indexed:',indexed,',u_name:',u_name,',user_name:',user_name         
          atu_reg2= "(1)id:"+str(id)+',indexed:'+str(indexed)+',u_name:'+str(u_name)+',user_name:'+str(user_name)         
          fcb_m.insert({ 'id': id,  'indexed': indexed,'u_name':u_name,'user_name':user_name })  
          indk1+=1
          cols['indexed']='S'
          fcb.insert(kl,cols)
          if indk1 > 25000: break
        
def process2():
 global atu_reg 
 global atu_reg2
 conn_mongo = pymongo.Connection(url_2)
 mongo_db = conn_mongo['mdnet1_2']
 fcb_m = mongo_db['fcb_users']
 indk1=1 
 index_cnts1=0
 for kl,cols in rest:
        #==============
        index_cnts1+=1
        id=cols['id']   
        indexed=cols['indexed']
        u_name=cols['u_name'] 
        user_name=cols['user_name']  
        if index_cnts1 % 1000 == 0 : 
          #print 'index_cnts1:',index_cnts1
          atu_reg='index_cnts1(2):'+str(index_cnts1)
        if indexed == 'N':        
          #print "id:",id,',indexed:',indexed,',u_name:',u_name,',user_name:',user_name         
          atu_reg2= "(2)id:"+str(id)+',indexed:'+str(indexed)+',u_name:'+str(u_name)+',user_name:'+str(user_name)         
          fcb_m.insert({ 'id': id,  'indexed': indexed,'u_name':u_name,'user_name':user_name })  
          indk1+=1
          cols['indexed']='S'
          fcb.insert(kl,cols)
          if indk1 > 25000: break

def process3():
 global atu_reg 
 global atu_reg2
 conn_mongo = pymongo.Connection(url_2)
 mongo_db = conn_mongo['mdnet1_3']
 fcb_m = mongo_db['fcb_users']
 indk1=1 
 index_cnts1=0
 for kl,cols in rest:
        #==============
        index_cnts1+=1
        id=cols['id']   
        indexed=cols['indexed']
        u_name=cols['u_name'] 
        user_name=cols['user_name']  
        if index_cnts1 % 1000 == 0 : 
          #print 'index_cnts1:',index_cnts1
          atu_reg='index_cnts1(3):'+str(index_cnts1)
        if indexed == 'N':        
          #print "id:",id,',indexed:',indexed,',u_name:',u_name,',user_name:',user_name         
          atu_reg2= "(3)id:"+str(id)+',indexed:'+str(indexed)+',u_name:'+str(u_name)+',user_name:'+str(user_name)         
          fcb_m.insert({ 'id': id,  'indexed': indexed,'u_name':u_name,'user_name':user_name })  
          indk1+=1
          cols['indexed']='S'
          fcb.insert(kl,cols)
          if indk1 > 25000: break

def process4():
 global atu_reg 
 global atu_reg2 
 conn_mongo = pymongo.Connection(url_2)
 mongo_db = conn_mongo['mdnet1_4']
 fcb_m = mongo_db['fcb_users']
 indk1=1 
 index_cnts1=0
 for kl,cols in rest:
        #==============
        index_cnts1+=1
        id=cols['id']   
        indexed=cols['indexed']
        u_name=cols['u_name'] 
        user_name=cols['user_name']  
        if index_cnts1 % 1000 == 0 : 
          #print 'index_cnts1:',index_cnts1
          atu_reg='index_cnts1(4):'+str(index_cnts1)
        if indexed == 'N':        
          #print "id:",id,',indexed:',indexed,',u_name:',u_name,',user_name:',user_name         
          atu_reg2= "(4)id:"+str(id)+',indexed:'+str(indexed)+',u_name:'+str(u_name)+',user_name:'+str(user_name)         
          fcb_m.insert({ 'id': id,  'indexed': indexed,'u_name':u_name,'user_name':user_name })  
          indk1+=1
          cols['indexed']='S'
          fcb.insert(kl,cols)
          if indk1 > 25000: break

def process5():
 global atu_reg 
 global atu_reg2
 conn_mongo = pymongo.Connection(url_2)
 mongo_db = conn_mongo['mdnet1_5']
 fcb_m = mongo_db['fcb_users']
 indk1=1 
 index_cnts1=0
 for kl,cols in rest:
        #==============
        index_cnts1+=1
        id=cols['id']   
        indexed=cols['indexed']
        u_name=cols['u_name'] 
        user_name=cols['user_name']  
        if index_cnts1 % 1000 == 0 : 
          #print 'index_cnts1:',index_cnts1
          atu_reg='index_cnts1(5):'+str(index_cnts1)
        if indexed == 'N':        
          #print "id:",id,',indexed:',indexed,',u_name:',u_name,',user_name:',user_name         
          atu_reg2= "(5)id:"+str(id)+',indexed:'+str(indexed)+',u_name:'+str(u_name)+',user_name:'+str(user_name)         
          fcb_m.insert({ 'id': id,  'indexed': indexed,'u_name':u_name,'user_name':user_name })  
          indk1+=1
          cols['indexed']='S'
          fcb.insert(kl,cols)
          if indk1 > 25000: break

process1()
process2()
process3()
process4()
process5()


        
        