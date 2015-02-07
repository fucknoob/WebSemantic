#EXEC
import mdER
import mdNeural
import umisc

import conn

conn= conn.conn_mx

def pmsg(msga):
 msg=''
 for m in msga:
  msg+=(' '+m)
 return msg


def post_l(usr,msga,source,referencias,sente):
 msg=msga
 sql1="delete from INBOX_MSG where USERNAME =? and source = ? "
 try:
   conn.sqlX (sql1,([usr,source]))
 except Exception,err: print 'Erro ao post(MSG_D):',err
 #======================================================================
 
 sql1="insert into INBOX_MSG(USERNAME,MSG,SOURCE,REFERENCIAS,SENTECE) values(?,?,?,?,?)"
 try:
   conn.sqlX (sql1,([usr,msg,source,referencias,sente]))
 except Exception,err: print 'Erro ao post(MSG_D):',err

  
def rem_results(usr,sente):
  sql1="delete from  INBOX_MSG where  USERNAME=? and  SENTECE = ?"
  try:
   conn.sqlX (sql1,([usr,sente]))
  except Exception,err: print 'Erro ao del(MSG_D):',err

def run( layers,relactionado,startL,usr,stack):
 print '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
 print 'kstermo:',stack.kstermo

 dts=[]
 dst_k=[]

 for cn in layers:
   if umisc.trim(cn.name) == "": continue

   print '---------------[',cn.name,']'
   

   fs=False
   
   for s in cn.topicos:
    if not s.dt[0] in dst_k:
     dst_k.append(s.dt[0])
    print '>>{',s.dt,'}'
    print '==========='
    for sr in s.sinapses:
     print 'dt:',sr.nr.dt
     for d1 in sr.nr.dt:
      if umisc.trim(d1) == '' :continue
      if d1 not in ['class']  :
       if umisc.trim(d1) != '':
         dts.append(d1)
       if umisc.trim(d1) != '' and  'identificador'  not  in s.dt :
         fs=True
    print '==========='
   print '---------------',fs
   

   if stack.kstermo !=  None:
     ds=''
     for d in dst_k:
      ds+=(d+' ')
     src='['+cn.name+']-'+ds
     # remover resultados
     if not stack.kstermo[1]:
      rem_results(usr,stack.kstermo[0])
     stack.kstermo[1]=True
     
     msg=pmsg(dts)
     msg=umisc.trim(msg)
     
     if msg == '' :return
     
     post_l(usr,msg,src,'',stack.kstermo[0])

     

 print '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'


