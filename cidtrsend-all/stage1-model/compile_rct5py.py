
import os
import sys
import umisc

import mdLayout
import mdER5
import mdNeural

import conn

conn= conn.conn_mx

connTrace=conn
conn4=conn
conn5=conn
conn3=conn

 
 

mdLayout.conn=conn

mdER5.conn=conn
mdER5.conn3=conn3
mdER5.conn4=conn4

mdNeural.conn=conn
mdNeural.conn3=conn
mdNeural.conn4=conn
 
 
usr=sys.argv[1]
print 'Process codepy....'
mdER5.process_py()
 
 
 
 