# testing question to mind-net

import sys
import os
import socket
import time
 
 

sock = socket.socket()          
host = '79.143.185.3'
 
port = 1295
 
sock.connect((host, port))
sock.send('RESET')
 
