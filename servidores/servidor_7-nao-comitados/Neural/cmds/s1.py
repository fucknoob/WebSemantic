
import sys
import socket
s=socket.socket()
host='srdfmailer01.bb.com.br'
port=25
s.connect((host,port))
print 'send helo'
s.send('HELO e-syns.com')
print s.recv(124)
#print 'send mail from'
s.send('MAIL FROM:<igor@e-syns.com>')
#print s.recv(124)
print 'send rcpt'
s.send('RCPT TO:<hayton.rocha@bb.com.br>')
#print s.recv(124)
print 'send data'
s.send('data')
print s.recv(124)
