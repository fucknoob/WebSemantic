#!/usr/bin/python           # This is client.py file
 
import socket                
 
s = socket.socket()          
host = '79.143.185.3'  
port = 1299                 
 
print 'Connecting to ', host, port
s.connect((host, port))
 
if True:
    #msg = raw_input('CLIENT >> ')
    msg='G'
    s.send(msg)
    msg = s.recv(1024)
    print 'ST: >> ', msg
