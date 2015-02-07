#

#EXEC
import mdER
import mdNeural
import umisc
import sys

sys.path.append('./pymongo')
sys.path.append('./pycassa')


import pycassa
from pycassa.pool import ConnectionPool
from pycassa import index
from pycassa.columnfamily import ColumnFamily
import pymongo
import bson

#============ base local de testes ============================

pool2 = ConnectionPool('MINDNET', ['localhost:9160'],timeout=10)
to_posting = pycassa.ColumnFamily(pool2, 'to_posting')
wb3 = pycassa.ColumnFamily(pool2, 'web_cache3')
to_posting2=pycassa.ColumnFamily(pool2, 'to_posting')
to_posting3=pycassa.ColumnFamily(pool2, 'to_posting')
to_posting5=pycassa.ColumnFamily(pool2, 'to_posting_perfil')

#=========== base producao  =============================

'''
MONGO_URL='mongodb://mdnet1:acc159753@91.205.172.85:27017/mdnet'
connMC = pymongo.Connection(MONGO_URL)
dbMC=connMC.mdnet
to_posting1=dbMC['to_posting']

'''
'''
pool2 = ConnectionPool('MINDNET', ['79.143.185.3:9160'],timeout=10000)
#to_posting2 = pycassa.ColumnFamily(pool2, 'to_posting')
to_posting3 = pycassa.ColumnFamily(pool2, 'to_posting2')
wb3 = pycassa.ColumnFamily(pool2, 'web_cache1')
'''
#================================================================

#import conn
#conn= conn.conn_mx

def pmsg(msga):
 msg=''
 for m in msga:
  msg+=(' '+m)
 return msg

def run( layers,relactionado,startL,usr,stack):
 print '{++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++}'
 print '{++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++}'
 print '{++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++}'
 print '{++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++}'
 print '{++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++}'
 print '{++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++}'
 idsb=mdNeural.GlobalStack.kstermo[0].split(' ')
 from_id=str(idsb)
 rl=''

 print 'stack.kstermo:',idsb
 for cn in layers:
  geral_uuid=0
  for s in cn.topicos:
    print '--------------layer.topico:uuid:',s.uuid  #
    geral_uuid=s.uuid
  if True:
   msg_id=0
   #=============================
   # teste e cassandra============
   r=wb3.get(str(geral_uuid))
   #== mongo
   #r2=wb3.find({'doc_id':str(geral_uuid)})
   # mongo precisa loop
   #for r in r2: # mongo
   if True: # cassandra
    print 'r->',r
    try:
     #mongo
     #lnk=r['DOC_ID2']
     #cassandra
     lnk=r['lomadee_url']
    except:
     try:
      #mongo
      #lnk=r['doc_id2']
      #Cassandra
      lnk=r['lomadee_url']
     except:
      try:
       lnk=r['DOC_ID']
      except:
       continue
    print 'link+pub:',lnk
    print 'from_id:',from_id
    # cassandra
    '''
    try:
     to_posting2.insert(from_id+'_'+str(geral_uuid)+str(lnk),{'from_id':from_id,'link_publish':lnk,'id_product':geral_uuid})
    except: pass
    '''
    try:
     to_posting5.insert(from_id+'_'+str(geral_uuid)+str(lnk),{'from_id':from_id,'link_publish':lnk,'id_product':geral_uuid})
    except: pass
    # mongo
    '''
    try:
     to_posting1.insert({'from_id':bson.Binary(from_id),'link_publish':bson.Binary(lnk),'id_product':bson.Binary(geral_uuid)})
    except: pass
    '''
  cn.dump_layer()
 print '{++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++}'
 print '{++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++}'
 print '{++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++}'
 print '{++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++}'
 print '{++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++}'
 print '{++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++}'




