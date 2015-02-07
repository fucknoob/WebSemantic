
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


def entry(usr):
 print 'start base table....'
 mdER5.process_base_tb()
 print 'Start compile:',usr
 mdER5.compile_rct(usr)
 conn.commit()
 
usr=sys.argv[1]
entry(usr) 
print 'term:OK'
print 'Processed:',mdER5.all_posted_objects
'''
print 'Resmume:=============================='
for s in mdER5.all_posted_log:
  print s,'\n'
 
''' 
ind=0
rk=mdER5.tb_object.get_range()
for k1,c1 in rk:
  ind+=1
print 'Post.objects:',ind  

print 'Process fz.load...'
mdER5.process_fzs()

print 'Process codepy....'
mdER5.process_py()
 
 
 
 