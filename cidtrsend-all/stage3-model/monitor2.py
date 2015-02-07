# monitor

import socket
import os
import MySQLdb
import thread

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("", 5001))
server_socket.listen(1000)

print "Mind-net Monitor Waiting for client on port 5001"


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
   cursor.execute ("SELECT msg from status_index  where USERNAME = %s  order by i desc",(usr))
   resultSet = cursor.fetchall()
   fnds=False
   for results in resultSet:
      fnds=True
      d=results[0]
      if  d == 'OK-FINAL3' or d == 'OK-FINAL2' or d == 'OK-FINAL' :
       dc=True
      break
   conn.close()
   if not fnds:
    dc=True
   return dc
   
 
def  reset_status(usr):
   rt=[]
   conn= MySQLdb.connect(host='dbmy0032.whservidor.com', user='mindnet_2' , passwd='acc159753', db='mindnet_2')
   cursor = conn.cursor ()
   cursor.execute ("delete from status_index where USERNAME = %s  ",(usr))
   cursor = conn.cursor ()
   cursor.execute ("delete from status_index_doc where USERNAME = %s  ",(usr))
   conn.close()   
   
def response(socket,dm):
 logid=socket.recv(512)
 usr=ret_usr(logid)
 susr=get_status_fin(usr)
 if susr :
  reset_status(usr)
  cmd1='python /home/mindnet/public_html/Neural/indexerUSR.py ' + ' "'+usr+'" ' 
  print 'Send cmd:',cmd1
  os.system(cmd1)
  #=====================
  cmd1='python /home/mindnet/public_html/Neural/SemaIndexerStage1.py ' + ' "'+usr+'" ' 
  print 'Send cmd:',cmd1
  os.system(cmd1) 

 
while 1:
 try:
     client_socket, address = server_socket.accept()
     print "Accept connection from ", address
     thread.start_new_thread(response,(client_socket,0))
 except Exception,e:
   print 'Error:',e
	
