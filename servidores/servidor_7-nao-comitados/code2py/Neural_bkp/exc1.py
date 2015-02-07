
import mdNeural


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
    obj_foco=[]
    #print 'N tops:' , len(layer.topicos)
    for t in layer.topicos:
        tp=t
        nr_t=t.dt[0]
        if len(tp.sinapses) >  1 :
         print '{',t.dt,'....','[',len(t.sinapses),']','}'
         if len(tp.sinapses) > 100:
          for ss in tp.sinapses:
           print ss.nr.dt
        if 'identificador' in t.dt:
         for sn in tp.sinapses:
          sn_dt=''
          for s1 in sn.nr.dt:
           sn_dt+=s1
          lay=mdNeural.mdLayer()
          lay.name=sn_dt
          objects.append(lay)
          obj_foco.append(lay)
        if 'realid2' in t.dt:
         print '{realid2}:',len(tp.sinapses)
         for sn in tp.sinapses:
          sn_dt=''
          for s1 in sn.nr.dt:
           sn_dt =s1
          lay=mdNeural.mdLayer()
          lay.name=sn_dt
          print '{{',sn_dt,'}}'
          lay.set_topico('identificador')
          lay.set_topico('{realid}')
          objects.append(lay)
          obj_foco.append(lay)
        #print 'obj:',sn_dt
    rel1=False
    for t in layer.topicos:
        topico_rsf=t
        #=======================================================
        ref_opcode=t.dt[0]
        if 'composicao' in t.dt or 'hierarchy' in t.dt :
          rel1=False
        #==============================================
        if ref_opcode in ['quality-good','need','way','guess','class','referencial','action','indicador','choice','decison','option','guess','state']:
          rel1=True
        if rel1:
            for sn in tp.sinapses:
             sn_dt=None
             for s1 in sn.nr.dt:
              sn_dt=s1
              break
             opc=ref_opcode
             for ob1 in obj_foco:
              referencia_c=False
              # referencia,link -> achar objeto e linkar , senao, apeas conecta
              if ref_opcode in ['refers','links','needs','ways','reference','referencial','referencia'] : referencia_c = True
              # ====
              if not referencia_c:
               ob1.set_topico_nr(topico_rsf)
              else :
               print '{Connect reference...}'
               obj_k=get_o(sn_dt)
               if obj_k == None:
                #criar obj
                obj_k=mdNeural.mdLayer()
                obj_k.name=sn_dt
               ob1.set_link_ds(obj_k,opc,[],[])

        #=============================================
        if 'composicao' in t.dt or 'hierarchy' in t.dt :
         sn_dt=''
         for ob1 in obj_foco:
          ob1.set_topico_nr(t)

    return objects


def run(lrc): # entry point
    return runc_layer(lrc)


    
retorno_srt=run(sr_int_cmd_param)