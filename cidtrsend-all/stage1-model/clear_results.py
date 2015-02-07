import os
import sys
import umisc

import conn
conn= conn.conn_mx


    
def clean(USERNAME):
 mt=[USERNAME]
 conn.sqlX(" delete from web_cache where usr=?   ", mt)
 conn.commit () 
 
 
     
def parse(s):
 r=''
 for d in s:
  kc=ord(d)
  if ( kc >= ord('a') and kc <= ord('z') ) or (kc >= ord('A') and kc <= ord('Z') )   or (kc >= ord('0') and kc <= ord('9') ) or d in ['.',',','!','?','\'','~','-']:
    r+=d
 return r

  
  
if len(sys.argv) > 1 :
 usr=parse(sys.argv[1])
 clean(usr)
   
 

conn.release()



print 'Process [OK]'