#EXEC

import mdNeural
import umisc


def runc_layer(layer,usr):
    return
    ref_opcode=''
    '''
    if True:
       print 'RTS(12):------------'
       r=layer
       for s in r.topicos:
         print 'Topico:',s.dt
         print 'SNS:++++++++++++++++++'
         for s1 in s.sinapses:
           print s1.nr.dt
         print '++++++++++++++++++'
       print 'RTS(12)(END):------------'
    '''

    obj_foco=[]
    i_quality=[]
    prop_l=False
    #print 'N tops:' , len(layer.topicos)
    topics=[]
    for t in layer.topicos:
      if 'tstatic' in t.dt : # se tstatic, avalia apenas os topicos abaixo desse
       for s1 in t.sinapses:
        topics.append(s1.nr)
      else:
        topics.append(t)

    for t in topics:
        tp=t
        nr_t=t.dt[0]
        if nr_t == '': continue
        if 'object' in t.dt or 'identificador' in t.dt :
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

    '''

    i_ev=[]
    i_ev_data=[]
    i_state=[]
    i_data_f=[]
    i_data_interv=[]
    i_ev_tps=[]


    dt_ini=None
    i_month=None
    i_year=None
    i_day=None
    for t in layer.topicos:
        topico_rsf=t
        rel1=False
        ref_opcode=t.dt[0]
        if 'object' in t.dt or 'identificador' in t.dt:
         continue
        #==============================================
        if 'quality' in t.dt:
         i_quality.append(t)
        if 'event' in t.dt:
         i_ev.append(t)
        elif 'event-data' in t.dt:
         i_ev_data.append(t)
        elif 'event-data' in t.dt :
         i_ev_data.append(t)

        elif 'event-data-month' in t.dt:
         i_month=(t)
        #=========================
        elif 'event-data-year' in t.dt:
         i_year=(t)
         i_data_f.append([i_day,i_month,i_year])
         i_day=None
         i_month=None
         i_year=None
        #=========================
        elif 'event-data-day' in t.dt:
         i_day=(t)
        #=========================

        elif 'state' in t.dt :
         i_state.append(t)
        elif 'event-data-ini' in t.dt :
         dt_ini=t
        elif 'event-data-end' in t.dt:
         if dt_ini != none:
          i_data_interv.append([dt_ini,t])
          dt_ini=None
        else:
          i_ev_tps.append(t)
          
        #==============================================


    #===========================================================================

    # mount event

    #===========================================================================

    cl_fnd=False
    cn_cl=[]
    ls_link =[]
    # ==
    for c_i in i_ev:
     # ==
     if prop_l:
      layer.topicos.remove(c_i)
     #====
     dt=c_i.dt
     # por classe e por caracts
     obs=layer.s_get_ontology_s(dt[0],[],[],usr )
     if len(obs)>0:
      cl_fnd=True
      for i in obs:
         ls_link.append(o)
     else:
      cn_cl.append(dt[0])
    if not cl_fnd:
     for dt in cn_cl:
      # procurar as informacoes nas caracts do obj
      obs=layer.s_get_ontology_s(dt,cn_cl,[],usr )
      if len(obs)>0:
        cl_fnd=True
        for i in obs:
         ls_link.append(o)

    if not cl_fnd:# criar um objeto __abstract__ e implementar com o class recolhido
           laycl=None
           if len(i_data_interv):
            for [ini,fim] in i_data_f:
              c_ini=''
              c_fim=''
              if ini != None:
               for s in ini.sinapses:
                for d in s.nr.dt:
                 if umisc.trim(c_ini) != '':
                  c_ini+=(' ')
                 c_ini+=( d  )
              #==
              if c_fim == None: continue
              for s in fim.sinapses:
                for d in s.nr.dt:
                 if umisc.trim(c_fim) != '':
                  c_fim+=(' ')
                 c_fim+=( d  )

            laycl=mdNeural.mdLayer()
            laycl.name=c_ini+'|'+c_fim
            ls_link.append(laycl)
    
           if len(i_data_f):
            for [day,month,year] in i_data_f:
              c_day=''
              c_month=''
              c_year=''
              if day != None:
               for s in day.sinapses:
                for d in s.nr.dt:
                 if umisc.trim(c_day) != '':
                  c_day+=(' ')
                 c_day+=( d  )
              #==
              if month != None:
               for s in month.sinapses:
                for d in s.nr.dt:
                 if umisc.trim(c_month) != '':
                  c_month+=(' ')
                 c_month+=( d  )
              #==
              if year == None: continue
              for s in year.sinapses:
                for d in s.nr.dt:
                 if umisc.trim(c_year) != '':
                  c_year+=(' ')
                 c_year+=( d  )

            laycl=mdNeural.mdLayer()
            laycl.name=c_day+'|'+c_month+'|'+c_year
            ls_link.append(laycl)
            
           elif len(i_ev):
             ev=''
             for y in i_ev:
               for s in y.sinapses:
                for d in s.nr.dt:
                 if umisc.trim(ev) != '':
                  ev+=(' ')
                 ev+=( d  )
                 
             laycl=mdNeural.mdLayer()
             laycl.name=ev
             ls_link.append(laycl)


           elif len(i_state):
             ev=''
             for y in i_state:
               for s in y.sinapses:
                for d in s.nr.dt:
                 if umisc.trim(ev) != '':
                  ev+=(' ')
                 ev+=( d  )

             laycl=mdNeural.mdLayer()
             laycl.name=ev
             ls_link.append(laycl)

           elif len(i_ev_data):
             ev=''
             for y in i_state:
               for s in y.sinapses:
                for d in s.nr.dt:
                 if umisc.trim(ev) != '':
                  ev+=(' ')
                 ev+=( d  )

             laycl=mdNeural.mdLayer()
             laycl.name=ev
             ls_link.append(laycl)

           if laycl!=None:
            for c_i in i_ev_tps:
             laycl.set_topico_nr(c_i)

    for la in obj_foco:
     for laycl in ls_link:
      if len(i_quality) == 0:
       la.set_link(laycl,'history')
      else:
       for q in i_quality:
        la.set_link(laycl,q.dt[0])


    
    for lr_p in obj_foco:
     if umisc.trim(lr_p.name) != '':
      print 'Prepare post object:',lr_p.name
      lr_p.s_post_object_by_data_es(lr_p,usr)

    return obj_foco




def run( layers,relactionado,startL,usr,stack):
  for lay in layers:
   rt=runc_layer(lay,usr)
  #return




