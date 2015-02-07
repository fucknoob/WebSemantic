#EXEC
import mdNeural
import umisc
import datetime as date2
import mdTb


def runc_layer(layer,usr):
    #===============================================
    def translate_year(mn):
     if mn == '$this-year':
      return str(date2.datetime.today().year)
     elif mn == '$next-year':
      return str(date2.datetime.today().year+1)
     elif mn == '$next-two-year':
      return str(date2.datetime.today().year+2)
     elif mn == '$next-three-year':
      return str(date2.datetime.today().year+3)
     elif mn == '$next-four-year':
      return str(date2.datetime.today().year+4)
     elif mn == '$next-five-year':
      return str(date2.datetime.today().year+5)
     elif mn == '$next-six-year':
      return str(date2.datetime.today().year+6)
     elif mn == '$next-seven-year':
      return str(date2.datetime.today().year+7)
     elif mn == '$next-eigth-year':
      return str(date2.datetime.today().year+8)
     elif mn == '$next-nine-year':
      return str(date2.datetime.today().year+9)
     elif mn == '$next-ten-year':
      return str(date2.datetime.today().year+10)
     else:
       return mn

    def translate_month(mn):
     if mn.lower() == 'janeiro':
      return 1
     elif mn.lower() == 'fevereiro':
      return 2
     elif mn.lower() == 'março' or mn.lower() == 'marco':
      return 3
     elif mn.lower() == 'abril':
      return 4
     elif mn.lower() == 'maio':
      return 5
     elif mn.lower() == 'junho':
      return 6
     elif mn.lower() == 'julho':
      return 7
     elif mn.lower() == 'agosto':
      return 8
     elif mn.lower() == 'setembro':
      return 9
     elif mn.lower() == 'outubro':
      return 10
     elif mn.lower() == 'novembro':
      return 11
     elif mn.lower() == 'dezembro':
      return 12
     else : return mn
    #===============================================
    not_in=['event','start','number','class-past','person','assunto','simple-collect','sample','equilibrio','know','mean','qtd-','time','indicative','interact','state','accept','way','need','intensity','grow','order','simple-','value','enum','event','news','referencial','compare','number','ele','ela']
    not_in2=['class-past','start-past']
    not_in3=['e','do','da','dos','das']
    not_in4=['state','event','start']
    ref_opcode=''
    global_uuid=0
    if True:
       print 'RTS(1--2-I)('+layer.name+'):------------'
       r=layer
       r.dump_layer()
       print 'RTS(1--2-I)(END):------------'

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

    i_need=[]
    i_sugest=[]
    i_guess=[]

    acts=[]
    event=[]

    for t in layer.topicos:
     reins_tps.append(t)


    start_data=None
    end_data=None
    for t in reins_tps:
        topico_rsf=t
        rel1=False
        ref_opcode=t.dt[0]
        dt1=''
        dt2=''
        #==============================================
        if ref_opcode in ['interact.state.moment.startday' ]  :
         for s in t.sinapses:
          for ds in s.nr.dt:
            d1=ds
            if ds != '': d1+='-'
            break
        #==============================================
        if ref_opcode in ['interact.state.moment.endday' ]  :
         for s in t.sinapses:
          for ds in s.nr.dt:
            d2=ds
            if ds != '': d2+='-'
            break
        #==============================================
        if ref_opcode in ['interact.state.moment.month' ]  :
         for s in t.sinapses:
          for ds in s.nr.dt:
            d1+=str(translate_month(ds))
            d2+=str(translate_month(ds))
            if ds != '':
             d2+='-'
             d1+='-'
            break
        #==============================================
        if ref_opcode in ['interact.state.moment.year' ]  :
         for s in t.sinapses:
          for ds in s.nr.dt:
            d1+=translate_year(ds)
            d2+=translate_year(ds)
            #===========
            start_data=d1
            end_data=d2
            #===========
            break
        #==============================================
        if ref_opcode in ['interact.state.moment' ] or ref_opcode in ['interact.state.moment.mult' ] :
          event.append(t)
        #==============================================
        if ref_opcode in ['need' ] or ref_opcode in ['interact.need' ] or ref_opcode in ['interact.info.value'] or ref_opcode in ['interact.want'] :
          i_need.append(t)
        #=============================================
        if ref_opcode in ['interact.can' ] or ref_opcode in ['interaction.comunic.ask.can'] or ref_opcode in ['interact.find'] or ref_opcode in ['interesting-ask'] :
          i_sugest.append(t)
        if  ref_opcode in ['interact.guess'] :
         i_guess.append(t)
        if ref_opcode in ['interact.get.action']  :
          acts.append(t)
        #==============================================
    #===========================================================================
    # need
    #===========================================================================
    cl_fnd=False
    cn_cl=[]
    ls_link =[]
    print 'Process need:',i_need
    if not cl_fnd:# criar um objeto __abstract__ e implementar com o class recolhido
           dtnm=''
           ah=False
           ah2=False
           to_class_impl=[]
           for c_i in i_need:
              for sn in c_i.sinapses:
                 to_class_impl.append(sn.nr)

           if True:
            print 'Parse need layers:',to_class_impl
            if len(to_class_impl) > 0 :
             laycl=mdNeural.mdLayer()
             laycl.name='[__need__]:'+str(global_uuid)
             #======================================================
             for cl_impl_nr in to_class_impl:
              tps=laycl.set_topico('defs')
              tps.uuid=global_uuid
              laycl.set_nr_ch_a2(tps,cl_impl_nr,'Composicao')
             for ev in event:
              laycl.set_topico_nr(ev)
             #======================================================
             for a in acts:
               c=laycl.set_topico_nr(a)
               c.uuid=global_uuid
             #======================================================
             if start_data!=None and end_data!=None:
                c=laycl.set_topico('interact.state.moment.start-data')
                c.uuid=global_uuid
                laycl.set_nr_ch(c,start_data,'defs')
                #============
                c=laycl.set_topico('interact.state.moment.end-data')
                c.uuid=global_uuid
                laycl.set_nr_ch(c,end_data,'defs')
             #=======================================================
             ls_link.append(laycl)

    print '[global_uuid]:',global_uuid
    for la in obj_foco:
     for laycl in ls_link:
      laycl.name=la.name+'[__need__]:'+str(global_uuid)
      print 'Process i_need link :',laycl.name
      la.set_link_ds(laycl,'need','','')

    #===========================================================================
    # guess
    #===========================================================================
    ls_link=[]
    cl_fnd=False
    cn_cl=[]
    ls_link =[]
    print 'Process guess:',i_guess
    if not cl_fnd:# criar um objeto __abstract__ e implementar com o class recolhido
           dtnm=''
           ah=False
           ah2=False
           to_class_impl=[]
           for c_i in i_guess:
              for sn in c_i.sinapses:
                 to_class_impl.append(sn.nr)

           if True:
            print 'Parse guess layers:',to_class_impl
            if len(to_class_impl) > 0 :
             laycl=mdNeural.mdLayer()
             laycl.name='[__guess__]:'+str(global_uuid)
             #======================================================
             for cl_impl_nr in to_class_impl:
              tps=laycl.set_topico('defs')
              tps.uuid=global_uuid
              laycl.set_nr_ch_a2(tps,cl_impl_nr,'Composicao')
             #======================================================
             for a in acts:
               r1=laycl.set_topico_nr(a)
               r1.uuid=global_uuid
             #======================================================
             ls_link.append(laycl)


    for la in obj_foco:
     for laycl in ls_link:
      laycl.name=la.name+'[__guess__]:'+str(global_uuid)
      print 'Process i_guess('+la.name+') link :',laycl.name
      la.set_link_ds(laycl,'guess','','')
   
    #===========================================================================
    # sugest
    #===========================================================================
    cl_fnd=False
    cn_cl=[]
    ls_link =[]
    print 'Process sugest:',i_sugest
    if not cl_fnd:# criar um objeto __abstract__ e implementar com o class recolhido

           dtnm=''
           ah=False
           ah2=False
           to_class_impl=[]
           for c_i in i_sugest:
              for sn in c_i.sinapses:
                 to_class_impl.append(sn.nr)

           if True:
            print 'Parse sugest layers:',to_class_impl
            if len(to_class_impl) > 0 :
             laycl=mdNeural.mdLayer()
             laycl.name='[__sugest__]:'+str(global_uuid)
             #======================================================
             for cl_impl_nr in to_class_impl:
              tps=laycl.set_topico('defs')
              tps.uuid=global_uuid
              laycl.set_nr_ch_a2(tps,cl_impl_nr,'Composicao')
             #======================================================
             for a in acts:
               c=laycl.set_topico_nr(a)
               c.uuid=global_uuid
             #======================================================
             ls_link.append(laycl)

    for la in obj_foco:
     for laycl in ls_link:
      laycl.name=la.name+'[__sugest__]:'+str(global_uuid)
      print 'Process i_sugest('+la.name+') link :',laycl.name
      la.set_link_ds(laycl,'sugest','','')

    #===========================================================================
    for lr_p in obj_foco:
     if umisc.trim(lr_p.name) != '':
      print 'Prepare post object:',lr_p.name
      az=mdTb.Zeus_Mode
      mdTb.Zeus_Mode=False
      lr_p.s_post_object_by_data_es(lr_p,usr)
      mdTb.Zeus_Mode=az
    return obj_foco

def run( layers,relactionado,startL,usr,stack):
  for lay in layers:
   rt=runc_layer(lay,usr)
  #return


