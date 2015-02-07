# monitor

import os
import sys
import MySQLdb


def  reset_status(usr):
   rt=[]
   conn= MySQLdb.connect(host='dbmy0032.whservidor.com', user='mindnet_2' , passwd='acc159753', db='mindnet_2')
   cursor = conn.cursor ()
   cursor.execute ("delete from status_index where USERNAME = %s  ",(usr))
   cursor = conn.cursor ()
   cursor.execute ("delete from status_index_doc where USERNAME = %s  ",(usr))
   conn.close()   
   
   
usr=sys.argv[1]
reset_status(usr)