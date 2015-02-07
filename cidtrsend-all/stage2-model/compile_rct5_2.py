
import os
import sys
import umisc

 
import mdER5_2
 

import conn

conn= conn.conn_mx

connTrace=conn
conn4=conn
conn5=conn
conn3=conn

 

mdER5_2.conn=conn
mdER5_2.conn3=conn3
mdER5_2.conn4=conn4

 


def entry(usr):
 print 'start base table....'
 mdER5_2.process_base_tb()
 print 'Start compile:',usr
 mdER5_2.compile_rct(usr)
 conn.commit()
 
usr=sys.argv[1]
entry(usr) 
print 'term:OK'
print 'Processed:',mdER5_2.all_posted_objects
'''
print 'Resmume:=============================='
for s in mdER5_2.all_posted_log:
  print s,'\n'
 
''' 
ind=0
rk=mdER5_2.tb_object.get_range()
for k1,c1 in rk:
  ind+=1
print 'Post.objects:',ind  

print 'Process fz.load...'
mdER5_2.process_fzs()

print 'Process codepy....'
mdER5_2.process_py()
 
 
 
 