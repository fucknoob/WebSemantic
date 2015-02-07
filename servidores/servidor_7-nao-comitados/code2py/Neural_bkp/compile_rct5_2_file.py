#coding:latin-1

import os
import sys
import umisc

 
import mdER5_2_file
 

def entry(usr):
 print 'start base table....'
 mdER5_2_file.process_base_tb()
 print 'Start compile rct:',usr
 mdER5_2_file.compile_rct(usr)
  
usr='igor.moraes'
entry(usr) 
#
print 'process_py...'
mdER5_2_file.process_py()

print 'All compile objects terminated!!!'
 
 
 
 