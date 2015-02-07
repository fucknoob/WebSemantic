import os
import time


def get_feeds( ):
 if True:
    try: 
     print 'Start process....'
     cmd='python32 superv_indexStage3.py  ' 
     os.system(cmd)
     #print cmd,'\n'
    except: pass 
    
    
    
while True:
  get_feeds()
  time.sleep(20)  
    
    
