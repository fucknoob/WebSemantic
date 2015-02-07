#!/usr/bin/python           # This is client.py file
 
import socket                
 
s = socket.socket()          
host = socket.gethostname()  
port=95

s.connect((host, port))
 
if True:
    msg='G'
    s.send(msg)
    msg = s.recv(1024)
    print 'RECV:', msg
