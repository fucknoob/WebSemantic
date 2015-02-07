#EXEC

def run( layers,relactionado,startL,usr,stack):
 for l in layers:
  for t in l.topicos:
   if l.s_compare_dt(t,'condition'):
    t.dt[0]='opcode'



