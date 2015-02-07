

import os
import time 

def start_job_sec( ):
  cmd='python windexer.py 0 1 > /home/mindnet/public_html/log1.txt'  
  print 'Prepare cmd:',cmd
  os.system(cmd)

  
  
while True:
    time.sleep(2)
    start_job_sec()