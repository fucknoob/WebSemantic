#!/usr/bin/python           # This is client.py file
 
import socket                
 
 
import time
startTT = time.clock ()
 
 
s = socket.socket()          
host = '79.143.185.3'  
port = 1302              
 
 
s.connect((host, port))
 
if True:
    incp=input('1-all|2-objects|3-No-Obj-Data:')
    s.send(str(incp))
    msg=''
    while msg != 'T':
     msg = s.recv(254)
     print msg

    
print 'End process.Time elapsed: ',time.clock () - startTT    