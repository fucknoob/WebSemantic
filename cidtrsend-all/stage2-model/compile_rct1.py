
import os
import sys
import umisc

import mdLayout
import mdER
import mdNeural

import conn

conn= conn.conn_mx

connTrace=conn
conn4=conn
conn5=conn
conn3=conn

 
 

mdLayout.conn=conn
mdER.conn=conn
mdER.conn3=conn3
mdER.conn4=conn4

mdNeural.conn=conn
mdNeural.conn3=conn
mdNeural.conn4=conn


def entry(usr):
 print 'Start compile:',usr
 mdER.compile_rct(usr)
 conn.commit()
 
usr=sys.argv[1]
entry(usr) 

 
 
 
 
 
 