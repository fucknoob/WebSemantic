#EXEC

import mdNeural
import umisc


def runc_layer(layer,ex_Data):
    objects=[]
    ref_opcode=''
    # Relaction-oper-opcode opcode original dos qualificadores se nao especificado
    #=====================================================
    def get_o_ob():
        for s in objects:
            if s.name==ob: return s
        return None
    #=====================================================
    class_fnd=False
    if True:
       print 'RTS(1EV-S):------------','[',ex_Data,']'
       r=layer
       for s in r.topicos:
         for kdt in s.dt:
          if ('event' in kdt  or 'startssssssss' in kdt ) and not 'event-stop' in kdt :
            class_fnd=True
            
          if 'object' in s.dt:
           for ds in s.sinapses:
            if ( 'event' in ds.nr.dt or 'startsssssssssss' in ds.nr.dt )and not 'event-stop' in ds.nr.dt:
             class_fnd=True


         print 'Topico:',s.dt
         print 'SNS:++++++++++++++++++'
         for s1 in s.sinapses:
           print s1.nr.dt
         print '++++++++++++++++++'
       print 'RTS(1EV-S)(END):------------'
    #===============================
    if not class_fnd:
     return
    obj_foco=[]
    #print 'N tops:' , len(layer.topicos)
    found_obj_1=False
    first_t=True
    lst=[]
    way_mid=False
    for t in layer.topicos:
       if first_t and 'indicador' in t.dt:
        pass
       elif 'event-link' in t.dt:
        pass
       elif 'object' in t.dt:
        pass
       elif 'way.mid' in t.dt:  #[way.mid,,way.mid]
        way_mid=True
        pass
       else:
            lst.append(t)
            
    for t in layer.topicos:
       if 'event-link' in t.dt and way_mid:
            lst.append(t)

    for t in layer.topicos:
        tp=t
        nr_t=t.dt[0]
        if nr_t == '': continue
        #======================================
        if (not first_t) and 'indicador' in t.dt:
          if len(obj_foco) > 0 :
           o=obj_foco[len(obj_foco)-1]
           t.dt=['pacient']
           o.set_topico_nr(t)

        #======================================  indicador em inicio de sentenca detem o significado de agente e object
        if ( ('event-link' in t.dt or 'start' in t.dt ) and not way_mid ) or 'way.mid' in t.dt :
         not_in=['alias','estimate','object3','place','class','indicador','indicator','defin','simple-collect','sample','equilibrio','know','mean','qtd-','time','indicative','interact','state','accept','way','need','intensity','grow','order','simple-','value','enum','event','news','referencial','compare','number','ele','ela']
         if way_mid :
          not_in=['alias','estimate','object3','place','class','indicador','defin','simple-collect','sample','equilibrio','know','mean','qtd-','time','indicative','interact','state','accept','need','intensity','grow','order','simple-','value','enum','event','news','referencial','compare','number','ele','ela']
         sn_dt=''
         
         for sn in t.sinapses:
          ah=False
          for a in sn.nr.dt:
            for cin in not_in:
             if cin in a.lower():
              ah=True
              continue
          if ah:
            continue
          email_ad=False
          for a in sn.nr.dt:
           if a in 'site-address':
            email_ad=True
          if email_ad:
           for k in sn.nr.sinapses:
            for k1 in k.nr.dt:
             sn_dt+=(k1)
          if not email_ad:
           for a in sn.nr.dt:
             sn_dt+=(a+' ')
           
         print 'T.dt:',t.dt ,'->[',sn_dt,']'
         if True:
          lay=mdNeural.mdLayer()
          lay.name=umisc.trim(sn_dt)
          #======================
          for topico_rsfd in lst:
           lay.set_topico_nr(topico_rsfd)
          lst=[]

          #====
          objects.append(lay)
          obj_foco.append(lay)


    return obj_foco


def run(lrc,ex_Data): # entry point
    return runc_layer(lrc,ex_Data)





