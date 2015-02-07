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
'''
pool2 = ConnectionPool('MINDNET', ['localhost:9160'],timeout=10)
to_posting = pycassa.ColumnFamily(pool2, 'to_posting')
'''
#=========== base mongo do amazon =============================


'''
MONGO_URL='mongodb://mdnet1:acc159753@ds061938.mongolab.com:61938/mdnet'
conn = pymongo.Connection(MONGO_URL)
dbM=conn.mdnet
to_posting=dbM['to_posting']
'''

#=========== base cassandra

'''
pool2 = ConnectionPool('MINDNET', ['79.143.185.3:9160'],timeout=10000)
to_posting = pycassa.ColumnFamily(pool2, 'to_posting')
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
 print '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
 print 'kstermo(2.1):',stack.kstermo
 print 'relactionado:',relactionado


 for cn in layers:
   #==============
   msg1=msg2=msg3=msg4=msg5=msg6=msg7=msg8=msg9=msg10=''
   if umisc.trim(cn.name) == "": continue
   print 'layer.to.see:'
   cn.dump_layer()
   dts=[]
   dts2=[]
   dts3=[]
   dst_k=[]

   print 'Layer.post[',cn.name,']'
   rts=cn.get_Reverse_links()
   refer_A=''
   refer_B=''
   print 'Referse.links:',rts,'==============='
   if len(rts)>0:
    for rev in cn.get_Reverse_links():
        refer_B=umisc.trim(rev.lr.name)
   print '=================================================='

   tags=[]
   fs=True
   geral_uuid=0
   for s in cn.topicos:
    print '--------------layer.topico:uuid:',s.uuid
    geral_uuid=s.uuid
    if not s.dt[0] in dst_k:
     dst_k.append(s.dt[0])
    if 'tag' in s.dt:
      for sr in s.sinapses:
       refer_Ac=''
       for l in sr.nr.dt:
        refer_Ac+=(' '+l)
       refer_Ac=umisc.trim(refer_Ac)
       tags.append(refer_Ac)
      continue
    if 'reference' in s.dt:
      for sr in s.sinapses:
       for l in sr.nr.dt:
        refer_A+=(' '+l)
      refer_A=umisc.trim(refer_A)
      continue
    if 'reference2' in s.dt:
      for sr in s.sinapses:
       for l in sr.nr.dt:
        refer_B+=(' '+l)
      refer_B=umisc.trim(refer_B)
      continue
    if 'identificador' in s.dt: continue
    if 'class' in s.dt : continue
    print '>>{',s.dt,'}'
    s1c2=s.dt
    print '==========='
    for sr in s.sinapses:
     print '   dt:',sr.nr.dt,'l:',len(sr.nr.dt)
     fnd_interact=False
     for d1 in sr.nr.dt:
      if 'interaction.get.action' in  d1:
       fnd_interact=True
       break
     if  fnd_interact:
      for s in sr.nr.sinapses:
       for ds in s.nr.dt:
         dts.append(ds)
     else:
      for d1 in sr.nr.dt:
       if umisc.trim(d1) != '':
         if d1 not in 'interaction.get.action':
           dts.append(d1)
         if d1 in 'state':
           dts2.append(d1)
         if d1 in 'dest':
           dts3.append(d1)
    print '==========='


   if stack.kstermo !=  None:
     #pool2 = ConnectionPool('MINDNET', ['localhost:9160'],timeout=10000)
     #w_cache3 = pycassa.ColumnFamily(pool2, 'web_cache3')
     #====================================================================
     print 'Mount.post!{..}',',d1:',dts,',d2:',dts2,',d3:',dts3,',refer_B:',refer_B
     ds=''
     for d in dst_k:
      ds+=(d+' ')
     if refer_A != '':
      src='['+cn.name+']-Original.Message('+refer_A+'.'+refer_B+')'
     else:
      src='['+refer_B+']-Sugest'
     # remover resultados
     if not stack.kstermo[1]:
      #rem_results(usr,stack.kstermo[0])
      pass
     stack.kstermo[1]=True

     msg1=pmsg(dts)
     msg1=umisc.trim(msg1)
     #
     msg2=pmsg(dts2)
     msg2=umisc.trim(msg2)
     #
     msg3=pmsg(dts3)
     msg3=umisc.trim(msg3)
     print 'geral_uuid:',geral_uuid
     print 'POST.MSG:',msg1,msg2,msg3
     #analizar o composition das msgs, pois deveram obedecer um layout de saida como msg a ser postada

     stack.tmp=[msg1,msg2,msg3]

     if msg1 == '' or len(tags) <=0 :return
     link=tags[0]
     msgp=msg1+' '+msg2+' '+msg3
     msgp=umisc.trim(msgp)

     #post_l(usr,src,'',stack.kstermo[0],msg1,msg2,msg3,msg4,msg5,msg6,msg7,msg8,msg9,msg10,geral_uuid)
     #geral_uuid->mensagem q originou o processamento
     #to_posting.insert(str(geral_uuid),{'msg':msgp,'from_uid:'geral_uuid,'link_oferta':link,'indexed':'N'})

 print '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'


