# monitor

import socket
import os
import MySQLdb

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("", 5005))
server_socket.listen(1000)

print "Mind-net Monitor Waiting for client on port 5005"



def  ret_usr(sessao):
   conn= MySQLdb.connect(host='dbmy0023.whservidor.com', user='mindnet' , passwd='acc159753', db='mindnet')
   cursor = conn.cursor ()
   cursor.execute ("SELECT USERNAME from usuarios where SESSAO= %s ",(sessao))
   resultSet = cursor.fetchall()
   for results in resultSet:
      i=results[0] 
      conn.close()
      return i
   conn.close()


   
def get_status_fin(usr):
   dc=False
   conn= MySQLdb.connect(host='dbmy0032.whservidor.com', user='mindnet_2' , passwd='acc159753', db='mindnet_2')
   cursor = conn.cursor ()
   cursor.execute ("SELECT msg from status_index3  where USERNAME = %s  order by i desc",(usr))
   resultSet = cursor.fetchall()
   fnds=False
   for results in resultSet:
      fnds=True
      d=results[0]
      if  d == 'OK-FINAL':
       dc=True
      break
   conn.close()
   if not fnds:
    dc=True
   return dc
   

def response(csocket,dmu):
 str1=csocket.recv(512)
 logid=''
 for s in str1:
  if s == '|' :  break
  logid+=s
 #====================== 
 usr=logid
 susr=get_status_fin(usr)
 if susr :
  cmd1='python /home/mindnet/public_html/Neural/SemaIndexerStage2.py ' + ' "'+str1+'"  & ' 
  print '[',cmd1,']'
  os.system(cmd1)
 #============================
 return 'CmdOK'

 
while 1:
 try:
     client_socket, address = server_socket.accept()
     print "Accept connection from (monitor-3)", address
     response(client_socket,0)
 except Exception,Err:
   print 'Erro.:',Err
   
   
	