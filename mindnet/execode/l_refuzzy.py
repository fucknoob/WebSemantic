#EXEC

import reFuzzy

def run( layers,relactionado,startL,usr,stack):
 objectives=[]
 for l in layers:
  # capturar dados de cada topico e gerar um fuzzy
  dts=[]
  for t in l.topicos:
   if l.s_compare_dt(t,'objective'):
    for d in t.sinapses:
     dt=''
     for d2 in d.nr.dt:
      dt+=(' '+d2)
     objectives.append(dt)
   else:
    dt=''
    for d in t.sinapses:
     for d2 in d.nr.dt:
      dt+=(' '+d2)
    dts.append(dt)
   #===
   ret=reFuzzy.entry(dts,objectives,usr)
   for r in ret:
    for ts in r.topicos:
     l.set_nr_ch_a(t,ts,'Composicao')
   
  # capturar opcodes de links, gerar fz e substituir esses opcodes por encontrados do processo fz
  # necessida dos objectives em pelo menos um layer
  if len(objectives) > 0:
   for lnk in l.links:
    dts=[]
    dts.append(lnk.opcode)
    for ds in lnk.opcode_seg:
     dts.append(ds)
    #===
    ret=reFuzzy.entry(dts,objectives,usr)
    for r in ret:
     # identificador => opcode
     # refer => opcode_seg
     ids=r.get_topico_s('Identificador')
     fir=False
     for i in ids:
      dt=''
      for d in i.dt:
       lnk.opcode=d
       if fir:
         l.set_link_ds(lnk.lr,d,'','')
       fir=True
     #============
     refers=r.get_topico_s('refer')
     dts=[]
     for i in ids:
      for d in i.dt:
       dts.append(d)
     #=====================
     nk.opcode_seg=dts
     

  

