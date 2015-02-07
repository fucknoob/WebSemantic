import os
import time


def get_feeds( ):
 if True:
    try: 
     print 'Start process....'
     cmd='python32 read_html.py  ' 
     os.system(cmd)
     #print cmd,'\n'
    except: pass 
    
    
time.sleep(5)    
while True:
  get_feeds()
  time.sleep(20)  
    
    
