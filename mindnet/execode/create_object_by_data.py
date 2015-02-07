#EXEC

import mdNeural
import umisc


def runc_layer(layer,usr):
    not_in=['event','start','number','class-past','person','assunto','simple-collect','sample','equilibrio','know','mean','qtd-','time','indicative','interact','state','accept','way','need','intensity','grow','order','simple-','value','enum','event','news','referencial','compare','number','ele','ela']
    not_in2=['class-past','start-past']
    not_in3=['e','do','da','dos','das']
    not_in4=['state','event','start']
    ref_opcode=''

    if True:
       print 'RTS(1--2):------------'
       r=layer
       for s in r.topicos:
         print 'Topico:',s.dt
         print 'SNS:++++++++++++++++++'
         for s1 in s.sinapses:
           print s1.nr.dt,len(s1.nr.sinapses)
         print '++++++++++++++++++'
       print 'RTS(1--2)(END):------------'


    obj_foco=[]
    prop_l=False
    abs_cnt=1
    #print 'N tops:' , len(layer.topicos)
    topics=[]
    reins_tps=[]
    for t in layer.topicos:
      if 'object' in t.dt or 'identificador' in t.dt:
        for sn in t.sinapses:
          ah=False
          for a in sn.nr.dt:
           for cin in not_in:
            if cin in a.lower():
             ah=True
             continue
          if ah:
           reins_tps.append(sn.nr)

    
    for t in layer.topicos:
      if 'tstatic' in t.dt : # se tstatic, avalia apenas os topicos abaixo desse
       for s1 in t.sinapses:
        topics.append(s1.nr)
      else:
        topics.append(t)
      
    found_by_name=False
    if True:
       if umisc.trim(layer.name) != '$$id$$' and umisc.trim(layer.name)!='':
         lay=mdNeural.mdLayer()
         lay.name=layer.name
         #===
         obj_foco.append(lay)
         found_by_name=True
      
    for t in topics:
        tp=t
        nr_t=t.dt[0]
        if nr_t == '': continue
        
        if 'object' in t.dt or 'identificador' in t.dt and not found_by_name:
         sn_dt=''
         for sn in tp.sinapses:
          for s1 in sn.nr.dt:

           print 'Object.fnd:',s1,'->>',t.dt
           sn_dt+=(s1+' ')
           
         rts=layer.s_get_ontology_ponderate(sn_dt,[],[],usr )
         for [ratting,la] in rts:
          obj_foco.append(la)
          break
         
         if len(rts) == 0:
          if umisc.trim(sn_dt) != '$$id$$':
           lay=mdNeural.mdLayer()
           lay.name=sn_dt
           #===
           obj_foco.append(lay)
           #===
    if len(obj_foco) == 0: # nao descreve um layer, é o proprio layer
      obj_foco.append(layer)
      prop_l=True
    '''
     composicao_register -> composicao => grava como topicos no objeto em 'identificador','object'
     abs_needs -> linka como need  objeto em 'identificador','object' com os elementos em abs_needs
     abs_way  -> linka como way  objeto em 'identificador','object' com os elementos em abs_way
     abs_mean  -> linka como mean  objeto em 'identificador','object' com os elementos em abs_mean
     abs_class  -> linka como class  objeto em 'identificador','object' com os elementos em abs_class
    '''

    i_composicao=[]
    i_class=[]

    i_defin=[]
    
    i_mean=[]
    i_orig=[] # contem as definicoes mean/class de interface( quais caracts implementam )

    
    i_owner=[]
    

    for t in layer.topicos:
     reins_tps.append(t)

    for t in reins_tps:
        topico_rsf=t
        rel1=False
        ref_opcode=t.dt[0]
        #=======================================================
        if 'composicao' in t.dt or 'hierarchy' in t.dt :
          i_composicao.append(t)
        #==============================================
        if ref_opcode in ['class' ]:
          i_class.append(t)
        #==============================================
        if ref_opcode in ['posse' ]:
          i_owner.append(t)
        #==============================================
        if ref_opcode in ['defin' ] or ref_opcode in ['defs' ]:
          i_defin.append(t)
        #==============================================
        if ref_opcode in ['orig' ]:
          i_orig.append(t)


    # aplica composicao
    for cm in i_composicao:
     # se for proprio objetc, remover os items descritivos
     if prop_l:
      layer.topicos.remove(cm)
      
     #====
     for ds in cm.sinapses:
       for obj_focos in obj_foco:
        tps=obj_focos.get_topico('defin')
        if tps == None:
         tps=obj_focos.set_topico('defin')
        tps.connect_to(tps.owner,ds.nr,'Composicao')



    #===========================================================================

    #   defin

    #===========================================================================
    print 'Process defin:',i_defin,'->foco:',obj_foco
    topicos=[]
    if len(obj_foco) > 0  and len(i_defin) > 0:
      for obj_focos in obj_foco:
       tps=obj_focos.get_topico('defin')
       if tps == None:
        tps=obj_focos.set_topico('defin')
       for id in i_defin:
        for k in id.sinapses:
         tps.connect_to(k.nr.owner,k.nr,'Composicao')
       topicos.append(tps)

    for cm in i_defin:
     if prop_l:
      layer.topicos.remove(cm)
     


    #===========================================================================
    
    #   class

    #===========================================================================
    cl_fnd=False
    cn_cl=[]
    ls_link =[]
    # procurar objetos,caracteristicas descritas em i_class
    print 'Process class:',i_class
    for c_i in i_class:
     # se for proprio objetc, remover os items descritivos
     try:
      if prop_l:
       layer.topicos.remove(c_i)
     except: pass
     #====
     dt=c_i.dt
     # por classe e por caracts
     obs=layer.s_get_ontology_s(dt[0],[],[],usr )
     #obs=[]
     if len(obs)>0:
      cl_fnd=True
      for i in obs:
         ls_link.append(o)
     else:
      cn_cl.append(dt[0])
    if not cl_fnd:
      for dts1 in cn_cl:
       # procurar as informacoes nas caracts do obj
       obs=layer.s_get_ontology_s(dts1,cn_cl,[],usr )
       if len(obs)>0:
         cl_fnd=True
         for i in obs:
          ls_link.append(o)

    if not cl_fnd:# criar um objeto __abstract__ e implementar com o class recolhido

           dtnm=''
           ah=False
           ah2=False

           to_class_impl=[]

           for c_i in i_class:
              for sn in c_i.sinapses:
               ah=False
               for a in sn.nr.dt:
                for cin in not_in:
                 if cin in a.lower():
                  ah=True
                  continue
                for cin in not_in2:
                 if cin in a.lower():
                  ah2=True
                  continue
               if ah:
                if not ah2:
                 to_class_impl.append(sn.nr)
                continue


               for d in sn.nr.dt:
                 dtnm+=(d+' ')

           if umisc.trim(dtnm) != '':
            worksc=[]
            tmpc=''
            for c in dtnm:
             if c == ' ' or c == ',':
              if c == ' ':
               worksc.append(c)
              worksc.append(tmpc)
              tmpc=''
             else:
              tmpc+=c
            if tmpc != '': worksc.append(tmpc)
            dtnm=[]
            tmpc=''
            print 'Parse class layers:',worksc
            for d in worksc:
                 if d.lower() == 'e' or d.lower() == ',' :
                  if umisc.trim(tmpc) != '':
                    dtnm.append(tmpc)
                  tmpc=''
                 else :
                  tmpc+=d
            if umisc.trim(tmpc) != '':
                  dtnm.append(tmpc)

            for dtnmc in dtnm:
             #print 'Postlr:',umisc.trim(dtnmc),'of:',not_in3
             if umisc.trim(dtnmc) not in not_in3:
              laycl=mdNeural.mdLayer()
              laycl.name=dtnmc

              for cl_impl_nr in to_class_impl:
                fr=False
                for d in cl_impl_nr.dt:
                  for l in not_in4:
                   if l in d :
                    fr=True
                if not fr:
                 laycl.set_topico_nr(cl_impl_nr)

              if len(i_orig) > 0 :
               top2=laycl.set_topico('orig')

               for sr  in i_orig:
                 laycl.set_nr_ch_a(top2,sr,'Composicao')
              

              ls_link.append(laycl)
            
    for la in obj_foco:
     for laycl in ls_link:
      print 'Process i_class link :',laycl.name
      la.set_link_ds(laycl,'class','','')



    #===========================================================================

    #   posse

    #===========================================================================

    cl_fnd=False
    cn_cl=[]
    ls_link =[]
    # procurar objetos,caracteristicas descritas em i_class
    print 'Process posse:',i_owner
    for c_i in i_owner:
     # se for proprio objetc, remover os items descritivos
     try:
      if prop_l:
       layer.topicos.remove(c_i)
     except: pass

    if not cl_fnd:# criar um objeto __abstract__ e implementar com o class recolhido

           dtnm=''
           ah=False
           ah2=False

           to_class_impl=[]

           for c_i in i_owner:
              for sn in c_i.sinapses:
               ah=False
               for a in sn.nr.dt:
                for cin in not_in:
                 if cin in a.lower():
                  ah=True
                  continue
                for cin in not_in2:
                 if cin in a.lower():
                  ah2=True
                  continue
               if ah:
                if not ah2:
                 to_class_impl.append(sn.nr)
                continue


               for d in sn.nr.dt:
                 dtnm+=(d+' ')

           if umisc.trim(dtnm) != '':
            worksc=[]
            tmpc=''
            for c in dtnm:
             if c == ' ' or c == ',':
              if c == ' ':
               worksc.append(c)
              worksc.append(tmpc)
              tmpc=''
             else:
              tmpc+=c
            if tmpc != '': worksc.append(tmpc)
            dtnm=[]
            tmpc=''
            print 'Parse class layers:',worksc
            for d in worksc:
                 if d.lower() == 'e' or d.lower() == ',' :
                  if umisc.trim(tmpc) != '':
                    dtnm.append(tmpc)
                  tmpc=''
                 else :
                  tmpc+=d
            if umisc.trim(tmpc) != '':
                  dtnm.append(tmpc)

            for dtnmc in dtnm:
             #print 'Postlr:',umisc.trim(dtnmc),'of:',not_in3
             if umisc.trim(dtnmc) not in not_in3:
              laycl=mdNeural.mdLayer()
              laycl.name=dtnmc

              for cl_impl_nr in to_class_impl:
                fr=False
                for d in cl_impl_nr.dt:
                  for l in not_in4:
                   if l in d :
                    fr=True
                if not fr:
                 laycl.set_topico_nr(cl_impl_nr)

              if len(i_orig) > 0 :
               top2=laycl.set_topico('orig')

               for sr  in i_orig:
                 laycl.set_nr_ch_a(top2,sr,'Composicao')


              ls_link.append(laycl)

    for la in obj_foco:
     for laycl in ls_link:
      print 'Process i_owner link :',laycl.name
      la.set_link_ds(laycl,'owner','','')

    #===========================================================================
    for lr_p in obj_foco:
     if umisc.trim(lr_p.name) != '':
      print 'Prepare post object:',lr_p.name
      lr_p.s_post_object_by_data_es(lr_p,usr)

    return obj_foco
    
    
    

def run( layers,relactionado,startL,usr,stack):
  for lay in layers:
   rt=runc_layer(lay,usr)
  #return
    
    
    
    
