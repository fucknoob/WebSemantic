#EXEC
import mdER
import mdNeural
import umisc

#import conn

#conn= conn.conn_mx

def pmsg(msga):
 msg=''
 for m in msga:
  msg+=(' '+m)
 return msg


def post_l2(usr,msga,source,referencias,sente):
 msg=msga
 print 'POST:',msg,source,referencias,sente
 sql1="delete from INBOX_MSG where USERNAME =? and source = ? "
 try:
   conn.sqlX (sql1,([usr,source]))
 except Exception,err: print 'Erro ao post(MSG_D):',err
 #======================================================================

 sql1="insert into INBOX_MSG(USERNAME,MSG,SOURCE,REFERENCIAS,SENTECE) values(?,?,?,?,?)"
 try:
   conn.sqlX (sql1,([usr,msg,source,referencias,sente]))
 except Exception,err: print 'Erro ao post(MSG_D):',err


def rem_results2(usr,sente):
  sql1="delete from  INBOX_MSG where  USERNAME=? and  SENTECE = ?"
  try:
   conn.sqlX (sql1,([usr,sente]))
  except Exception,err: print 'Erro ao del(MSG_D):',err


def rem_results(usr,sente):
  sql1="delete from  table1_result where  USERNAME=? and  SENTECE = ?"
  try:
   conn.sqlX (sql1,([usr,sente]))
  except Exception,err: print 'Erro ao del(MSG_D):',err


def post_l(usr,source,referencias,sente,msg1,msg2,msg3,msg4,msg5,msg6,msg7,msg8,msg9,msg10,geral_uuid):
 print 'POST:',source,referencias,sente,msg1,msg2,msg3,msg4,msg5,msg6,msg7,msg8,msg9,msg10
 sql1="delete from table1_result where USERNAME =? and source = ? "
 try:
   conn.sqlX (sql1,([usr,source]))
 except Exception,err: print 'Erro ao post(MSG_D):',err
 #======================================================================
 print 'geral.uuid:',geral_uuid
 post=''
 gins=conn.sqlX('select pg from web_cache3 where i=?' ,[geral_uuid] )
 for e in gins:
  post=e[0].read()
  break
  
 if post == '':
  gins=conn.sqlX('select pg from web_cache where i=?' ,[geral_uuid] )
  for e in gins:
   post=e[0].read()
   break

 sql1='insert into table1_result(USERNAME,SOURCE,REFERENCIAS,SENTECE,ql1,ql2,ql3,ql4,ql5,ql6,ql7,ql8,ql9,ql10,post)'
 sql1+=' values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
 #sql1="insert into INBOX_MSG(USERNAME,MSG,SOURCE,REFERENCIAS,SENTECE) values(?,?,?,?,?)"
 try:
   conn.sqlX (sql1,([usr,source,referencias,sente,msg1,msg2,msg3,msg4,msg5,msg6,msg7,msg8,msg9,msg10,post]))
 except Exception,err: print 'Erro ao post(MSG_D):',err
 conn.commit()



#===============================================================================
#===============================================================================


def run( layers,relactionado,startL,usr,stack):
 print '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
 print 'kstermo(2.1):',stack.kstermo


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


   fs=True
   geral_uuid=0
   for s in cn.topicos:
    print '--------------layer.topico:uuid:',s.uuid
    geral_uuid=s.uuid
    if not s.dt[0] in dst_k:
     dst_k.append(s.dt[0])
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
     print 'Mount.post!{..}',',d1:',dts,',d2:',dts2,',d3:',dts3
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
     print 'POST.MSG:',msg1,msg2,msg3

     stack.tmp=[msg1,msg2,msg3]

     if msg1 == '' :return

     #post_l(usr,src,'',stack.kstermo[0],msg1,msg2,msg3,msg4,msg5,msg6,msg7,msg8,msg9,msg10,geral_uuid)


 print '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'


