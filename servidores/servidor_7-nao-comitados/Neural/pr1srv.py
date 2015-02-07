
import os
import sys
import time
 

def run_cmd_s():
 while True:
    try: 
     print 'Start process....'
     cmd='python32 friends1.py '
     os.system(cmd)
    except: pass 
    print 'Process:',' finished'   
    time.sleep(5*60) # 5 minnutos

  
run_cmd_s()
    