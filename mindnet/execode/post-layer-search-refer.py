#EXEC

import mdNeural
import umisc


def runc_layer(layer):
    objects=[]
    ref_opcode=''
    # Relaction-oper-opcode opcode original dos qualificadores se nao especificado
    #=====================================================
    def get_o_ob():
        for s in objects:
            if s.name==ob: return s
        return None
    #=====================================================

    if True:
       print 'RTS-REF(1):------------'
       r=layer
       for s in r.topicos:
         print 'Topico:',s.dt
         print 'SNS:++++++++++++++++++'
         for s1 in s.sinapses:
           print s1.nr.dt
         print '++++++++++++++++++'
       print 'RTS-REF(1)(END):------------'

    obj_foco=[]
    #print 'N tops:' , len(layer.topicos)
    for t in layer.topicos:
        tp=t
        nr_t=t.dt[0]
        if nr_t == '': continue
        if 'referencial.source' in t.dt :
         sn_dt=''
         for sn in tp.sinapses:
          if 'indicador' not in sn.nr.dt:
           for s1 in sn.nr.dt:
            sn_dt+=(s1+' ')
           
         if umisc.trim(sn_dt) != '$$id$$' and umisc.trim(sn_dt) != '':
          print 'referencial.source:',sn_dt
          if len(obj_foco) > 0:
           lay=obj_foco[0]
           lay.name+=(sn_dt)
          else:
           lay=mdNeural.mdLayer()
           lay.name=sn_dt
           #====
           objects.append(lay)
           obj_foco.append(lay)
    rel1=False
    for t in layer.topicos:
       topico_rsf=t
       #==============================================
       for dt_top in topico_rsf.dt:
        if dt_top in [ 'referencial'] or ref_opcode in [ 'refer']:
             for ob1 in obj_foco:
              ob1.set_topico_nr(topico_rsf)
             break
    print 'Obj.foco.refer:',obj_foco
    return obj_foco


def run(lrc,ex_Data): # entry point
    return runc_layer(lrc)



