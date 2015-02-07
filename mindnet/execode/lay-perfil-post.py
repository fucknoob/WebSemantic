#EXEC
import mdER
import mdNeural

def run(layers,relacionado,startL,usr,stack):
 print 'Start layoutcode:-------------'
 '''
 #----------re call other rct
 rcts_to_call=[]
 m=mdNeural.mdLayer()
 m.name='perfil-reputacao'
 layers_to_result=[]
 for l in layers:
  # achar sequencia de guess,options e gerar sentenca,result in layers_to_result,
  pass
 #conferir se tem outras rct a ser chamadas para complementar , em to_c
 for to_c in rcts_to_call:
  rcts_second_1=mdEr.get_RactionLines(to_c,usr)
  rcts_second=[]
  for s in rcts_second_1:
   for l in s:
     if type(l).__name__ == 'instance':
      if l.__class__.__name__ == 'mdLayer':
        rcts_second.append(l)

  #==================================================
  for rct in rcts_second:
   for pr in layers_to_result:
    rts=rct.process_RCT(pr,None,usr,to_c)
 '''
 # post layers_to_result em inbox_msg2,inbox_msg ou clipping_return


