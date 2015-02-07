import sys
import os


import bson

import pymongo

#file:200

print 'Connect to mongo...'
MONGO_URL='mongodb://mdnet1:acc159753@127.0.0.1:27017/mdnet'
connM = pymongo.Connection(MONGO_URL) 
dbM=connM.mdnet
fcbM=dbM['fcb_users']


fil=sys.argv[1]


if str(fil) == '99999':
 fcbM.remove()
else:
 cache=[]
 
 class clineb:
  def __init__(self):
   self.id=''
   self.indexed=''
   self.user_name=''
   self.u_name=''
   self.key=''
  def prints(self):
   print 'key:',self.key,',user_name:',self.user_name,',u_name:',self.u_name,',uid:',self.id,',indexed:',self.indexed 
  def process_line(self,ln):
    tmp=''
    for k in ln:
     if k == '|' :
      if self.key =='':
       self.key=tmp
      elif self.user_name=='': 
       if tmp == '': tmp='-'
       self.user_name=tmp
      elif self.id =='':
       self.id=tmp
      elif self.u_name == '':
       if tmp == '': tmp='-'
       self.u_name=tmp
      else:
       self.indexed=tmp
      tmp='' 
     else:
      tmp+=k
    if tmp!= '':
      self.indexed=tmp   
    if self.indexed!= '':  
     self.indexed=self.indexed[0]
 
 file=open('/usrOK/'+str(fil),"r")
 print 'Start to collect.....'
 while 1:
     line = file.readline()
     if not line:
       break
     lin=clineb()
     lin.process_line(line)    
     cache.append(lin)
     #
     if len(cache) % 10000 ==0 : print 'cnt:',len(cache)
 
 file.close()    
 
 
      
 ind=0
 for ca in cache:
   ind+=1
   #ca.prints()
   #
   #
   fcbM.insert({"_id":ca.id,"id":ca.id,"indexed":'N',"user_name":bson.Binary(ca.user_name),"u_name":bson.Binary(ca.u_name),"process":str(fil)}) 
   if ind % 10000 == 0 : print 'Save:',ind   
 
print 'total inserts:',fcbM.count()
      
  