#encoding:latin-1
import urllib2,urllib, cookielib, re, os, sys
import urllib
import umisc


import sys, os
import Pyro.core

import thread
import socket

from Pyro.errors import PyroError

products_client=[]

def gerate_insert_client(cli,prod,rc):
     fndp=False 
     global products_client
     for [client1,prod1] in products_client:
          if client1 == cli:
               fndp=True
               fnd=False
               for [prod2,rc2] in prod1:
                    if prod2==prod:
                         fnd=True
               if not fnd:
                    prod1.append([prod,rc])
     if not fndp:
          products_client.append( [cli,[ [prod,rc] ]  ]) 

def collect_vitrines():
     import pycassa
     from pycassa.pool import ConnectionPool
     from pycassa.columnfamily import ColumnFamily
     from pycassa import index
     pool2 = ConnectionPool('MINDNET', ['79.143.185.3:9160'],timeout=100000)
     tab2 = pycassa.ColumnFamily(pool2, 'cache_products')     
     pub = pycassa.ColumnFamily(pool2, 'to_posting2') 
     wb2 = pycassa.ColumnFamily(pool2, 'web_cache1') # lugar para indexar
     #=================================     
     counter=0     
     for ky,col in pub.get_range(): 
          prods=col['id_product'].decode('hex')
          rc=tab2.get(prods)  
          from_id3=col['from_id']
          from_id3=from_id3.replace('\'','')
          from_id3=from_id3.replace('[','')
          from_id3=from_id3.replace(']','')
          from_id2=from_id3.split(',' )
          from_id=''
          for ifr in from_id2:
               ifr=umisc.trim(ifr)
               if len(ifr) > 1:
                    if ifr[0] in ['0','1','2','3','4','5','6','7','8','9'] and ifr[1] in ['0','1','2','3','4','5','6','7','8','9']:
                         from_id=ifr 
                         break
          counter+=1
          col['id_post']=str(counter)
          url_lomadee=rc['lomadee_url']
          pub.insert(ky,col)
          prod=rc['cod_p'] 
          rccc=wb2.get(prods.encode('hex'))
          rccc['lomadee_url']=rc['lomadee_url']
          #
          gerate_insert_client(from_id,prod,rccc)
          #============================
     return products_client   

itrs=collect_vitrines()


class layoutBean(Pyro.core.ObjBase):
     def __init__(self):
          Pyro.core.ObjBase.__init__(self)
     def reset(self):
          global itrs
          itrs=collect_vitrines()
     def get_users(self):  
          global itrs        
          #================ 
          return itrs


Pyro.core.initServer()

daemon = Pyro.core.Daemon(port=38)
print
print 'The Pyro Deamon is running on ',daemon.hostname+':'+str(daemon.port)
print '(you may need this info for the client to connect to)'
print

objectName='layoutBean'

#uri=daemon.connect(layoutBean(),objectName)

object=Pyro.core.ObjBase()  # delegate approach
object.delegateTo(layoutBean())

uri=daemon.connect(object,objectName)

# enter the service loop.
print 'layoutBean is ready for customers.'
print 'Object name is:',objectName
print 'The URI is: ',uri

daemon.requestLoop()




