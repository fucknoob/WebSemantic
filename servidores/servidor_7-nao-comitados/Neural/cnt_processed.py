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

import conn
conn= conn.conn_mx

import datetime
import time, datetime


usr2='igor.moraes'

def init_nums_i():
  try:
     sq="select count(*) from web_cache3 where USR='"+usr2+"' and (indexed='S') "
     cursor = conn.sql (sq)
     for results in cursor:
        I=results[0]
        print 'Rows:',I
           
  except Exception,e : 
   print 'Error:',e
    
          

init_nums_i()
