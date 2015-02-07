#coding: latin-1

import simplejson
import urllib
import os
import sys
import urllib2
import umisc
import gc
import thread
import time

import conn3
conn= conn3.conn_mx

import datetime
import time, datetime


usr2='igor.moraes'

def init_nums_i():
  try:
     sq="select rowcount from tablesize where tablename ='WEB_CACHE3_IDX' "
     cursor = conn.sql (sq)
     for results in cursor:
        I=results[0]
        print 'Rows:',I
           
  except Exception,e : 
   print 'Error:',e
    
          

init_nums_i()
