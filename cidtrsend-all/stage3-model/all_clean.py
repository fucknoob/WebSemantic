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

usr2='igor.moraes'

def clean_all():
  global usr2
  sq="update web_cache3 set indexed='N' where USR='"+usr2+"'  "
  cursor = conn.sql (sq)
  #==================
  sq=" delete from WEB_CACHE3_IDX2__2  "
  cursor = conn.sql (sq)
  #==================
  sq=" delete from WEB_CACHE3_IDX  "
  cursor = conn.sql (sq)
  #==================
  sq=" delete from WEB_CACHE3_IDX2  "
  cursor = conn.sql (sq)
  conn.commit()          
 
clean_all()

 
 
 
     
     


