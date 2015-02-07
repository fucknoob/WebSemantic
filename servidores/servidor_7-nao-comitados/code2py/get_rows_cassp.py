#!/usr/bin/python           # This is client.py file
 
import socket                
 
tp=input("1:Zeus3|2:Zeus4\n=")
tp=str(tp) 
 
s = socket.socket()          
host = socket.gethostname()  

cant=''
cpos=''
hasj=False
if '|' in tp:
 hasj=True
 for d in tp:
  if d =='|':
     cant=tmp
     tmp=''
  else:
   tmp+=d  
  cpos=tmp 

if hasj:
 tp=cant  
  
if tp == '2':
 port = 12244                 
elif tp == '1' :
 port = 12243
else :
 raise Exception("Not selected[1/2]")
  
  
  
print 'option:',tp
s.connect((host, port))
 
if True:
    msg='G'
    if hasj :
      msg=cpos
    s.send(msg)
    msg = s.recv(1024)
    print 'RECV:', msg
