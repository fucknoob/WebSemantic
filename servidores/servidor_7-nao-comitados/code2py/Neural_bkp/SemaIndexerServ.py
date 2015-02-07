
import os
import sys
import time
import thread

class thread_cntl:
 def __init__(self):
  self.finished=False

def remp(s):
 r=''
 i=len(s)-1
 pos=0
 while i >= 0 :
  if s[i] == '\\' or s[i] == '/': 
   pos=i
   break
  r=s[i]+r
  i-=1
 return s[:pos+1]  
  
pth=remp(sys.argv[0])  

def run_cmd_s(d,th):
 while True:
    try:
     print 'Start process.................'
     cmd='/Neural/runs_ch2 > log.txt ' 
     #print cmd
     os.system(cmd)
    except: pass 
    print 'Process:',' finished'   

   

def call_links(usr):
  i=0
  ths=[]
  #while i < 20:
  if True:
   print 'Start indexer '+str(i)
   #proc = subprocess.Popen("/home/mindnet/public_html/dpsearch/sbin/indexer  ", shell=True,stdout=subprocess.PIPE)
   #proc = subprocess.Popen("/home/esyns1/public_html/dpsearch/sbin/indexer  ", shell=True,stdout=subprocess.PIPE)
   ths.append(thread_cntl())
   thread.start_new_thread(run_cmd_s,(usr,ths[len(ths)-1] ) )
   time.sleep(10)
   i+=1

  ind_col=0
  while True:
   print 'wait for pages...',len(ths)-ind_col
   fnds_t=False
   ind_col=0
   for ths1 in ths:    
    if not ths1.finished:fnds_t=True
    if ths1.finished: ind_col+=1
   if fnds_t:
    time.sleep(10)
    continue
   else:
    break   

usr=''
#usr=(sys.argv[1])   
call_links(usr)

    