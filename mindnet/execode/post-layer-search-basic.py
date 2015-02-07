#EXEC

import mdNeural
import umisc

def parse_t(s):
 rt=[]
 tmp=''
 for i in s:
  if i == ' ':
   rt.append(tmp)
   tmp=''
  else:
   tmp+=i
 if tmp != '':
  rt.append(tmp)
 return rt
 
def c_in(s,arr):
 for d in arr:
  if s == d: return True
 return False

def sep_multiple_data_unkwon(dt):
 dts=parse_t(dt)
 l=len(dts)-1
 rt=[]
 while l >=0 :
  if dts[l] in ['o','a','os','as']:
    rt.insert(0,dts[l])
    break
  rt.insert(0,dts[l])
  l-=1
 c=''
 for r in rt:
   c+=(' '+r)
 return umisc.trim(c)


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
       print 'RTS(1-S):------------','[',ex_Data,']'
       r=layer
       for s in r.topicos:
         if 'class' in s.dt or 'classe' in s.dt or 'classificacao' in s.dt or 'defs' in s.dt  :
          class_fnd=True
         if 'object' in s.dt:
          for ds in s.sinapses:
           if 'class' in ds.nr.dt or 'classe' in ds.nr.dt or 'classificacao' in ds.nr.dt or 'defs' in ds.nr.dt :
            class_fnd=True

         print 'Topico:',s.dt
         print 'SNS:++++++++++++++++++'
         for s1 in s.sinapses:
           print s1.nr.dt
         print '++++++++++++++++++'
       print 'RTS(1-S)(END):------------'
    #===============================
    print 'class_fnd:',class_fnd
    if not class_fnd:
     return
    obj_foco=[]
    ex_Data2=[]
    #print 'N tops:' , len(layer.topicos)
    found_obj_1=False
    first_t=True
    for t in layer.topicos:
        tp=t
        nr_t=t.dt[0]
        if nr_t == '': continue
        #======================================
        if (not first_t) and 'indicator' in t.dt:
          if len(obj_foco) > 0 :
           o=obj_foco[len(obj_foco)-1]
           t.dt=['pacient']
           o.set_topico_nr(t)
           
        #======================================  indicador em inicio de sentenca detem o significado de agente e object
        if first_t and 'indicator' in t.dt:
         sn_dt=''
         lst=[]
         t.dt=['agent']
         for sn in tp.sinapses:
          ah=False
          for a in sn.nr.dt:
           if 'way' in a:
            ah=True
            continue
           if 'simple-collect' in a:
            ah=True
            continue
          if ah: continue

          if  'intensity' in sn.nr.dt:
            lst.append(sn.nr)
            continue
          for s1 in sn.nr.dt:
           if umisc.trim(s1) in [',',';','.','?','!','with','e','E','dos','das','do','da']:
             s1=''
           sn_dt+=(s1+' ')

         if umisc.trim(sn_dt) != '$$id$$':
          lay=mdNeural.mdLayer()
          if umisc.trim(sn_dt) in [',',';','.','?','!','with','e','E','dos','das','do','da']:
           sn_dt=''
          sn_dt=sn_dt.replace(',','')
          sn_dt=sn_dt.replace('.','')
          sn_dt=sn_dt.replace(';','')
          sn_dt=sn_dt.replace('!','')
          sn_dt=sn_dt.replace('?','')
          sn_dt=sn_dt.replace('"','')
          if umisc.trim(sn_dt).lower() == 'e' :
           sn_dt=''

          lay.name=umisc.trim(sn_dt)

          if umisc.trim(sn_dt) == '':
           if len(ex_Data) > 0   :
             print 'ex_Data(1)-->',ex_Data
             for s in ex_Data:
              if umisc.trim(s.name) != '':
               lay.name = s.name
               break


          for topico_rsfd in lst:
           lay.set_topico_nr(topico_rsfd)
          lay.set_topico_nr(t)
          #====
          objects.append(lay)
          obj_foco.append(lay)
          ex_Data.append(lay)
          found_obj_1=True

        #===================================================
        if 'object' in t.dt :
         sn_dt=''
         lst=[]
         not_in=['alias','object3','class','indicator','defin','simple-collect','sample','equilibrio','know','mean','qtd-','time','indicative','interact','state','accept','way','need','intensity','grow','order','simple-','value','enum','event','news','referencial','compare','number']
         for sn in tp.sinapses:
          ah=False
          for a in sn.nr.dt:
           for cin in not_in:
            if cin in a.lower() and a.lower() != 'evento' and a.lower() != 'eventos':
             ah=True
             continue
          if ah:
           lst.append(sn.nr)
           continue

          if 'place' in sn.nr.dt:
            lst.append(sn.nr)
            sn_dt=''
            for sn2 in sn.nr.sinapses:
             for a in sn2.nr.dt:
               sn_dt+=(' '+a)

            if umisc.trim(sn_dt) != '$$id$$' and len(ex_Data2)==0:
             lay=mdNeural.mdLayer()
             new_k=sn_dt
             lay.name= umisc.trim(new_k)
             if umisc.trim(sn_dt) == '':
              if len(ex_Data) > 0   :
                print 'ex_Data(1.2)-->',ex_Data
                for s in ex_Data:
                 if umisc.trim(s.name) != '':
                  lay.name = s.name
                  break
             #====
             objects.append(lay)
             #
             lay.name=sep_multiple_data_unkwon(lay.name)
             #
             obj_foco.append(lay)
             ex_Data.append(lay)
             ex_Data2.append(lay)
             #
            else:
             lay=ex_Data2[0]
             lay.name+=(sn_dt)
            #==============================================
            for topico_rsfd in lst:
              lay.set_topico_nr(topico_rsfd)
            topico_rsfd=[]
            continue

          if ('simple-collect-place2' in sn.nr.dt) or ('place-this' in sn.nr.dt) or ('place' in sn.nr.dt) :
            lst.append(sn.nr)
            continue
          if  ('intensity' in sn.nr.dt) or ('person' in sn.nr.dt) or ('event' in sn.nr.dt) :
            lst.append(sn.nr)
            continue
          for s1 in sn.nr.dt:
           if umisc.trim(s1) in [',','"']:
            s1=''
           sn_dt+=(s1+' ')

         if umisc.trim(sn_dt) != '$$id$$':
          lay=mdNeural.mdLayer()

          new_k=sn_dt
          lay.name= umisc.trim(new_k)
          
          if umisc.trim(sn_dt) == '':
           if len(ex_Data) > 0   :
             print 'ex_Data(1)-->',ex_Data
             for s in ex_Data:
              if umisc.trim(s.name) != '':
               lay.name = s.name
               break

          
          for topico_rsfd in lst:
           lay.set_topico_nr(topico_rsfd)
          #====
          #print 'lay-name:',lay.name
          objects.append(lay)
          
          # verificar se tem mais de 3 words no nome do objeto, restringir ate achar ['o','a']
          lay.name=sep_multiple_data_unkwon(lay.name)
          
          obj_foco.append(lay)
          ex_Data.append(lay)
          found_obj_1=True
        first_t=False
    if len(obj_foco) > 0 and (not found_obj_1) :
          print 'ex_Data-->',obj_foco
          lay= obj_foco[ len(obj_foco)-1 ]
          for topico_rsfd in lst:
           lay.set_topico_nr(topico_rsfd)
           
    elif len(ex_Data) > 0 and (not found_obj_1) :
       print 'ex_Data-->',ex_Data
       
    rel1=False
    # verificar se tem os campos mandatorios( caracts necessarias )
    mdn=False
    for t in layer.topicos:
        topico_rsf=t
        rel1=False
        #=======================================================
        ref_opcode=t.dt[0]
        
        #==============================================
        if ref_opcode not in ['',None,'object' ]:
             for ob1 in obj_foco:
              ob1.set_topico_nr(topico_rsf)
        #=============================================
    if not mdn and layer in obj_foco:
     obj_foco.remove(layer)

    '''
    print 'DUMP:------------------!!'
    for ok in obj_foco:
     for te in ok.topicos:
       print 'TP:-------------'
       print te.dt
       print 'SNS:','-----------'
       for sg in te.sinapses:
         print sg.nr.dt
       print 'TP(END):-------------'
    print '-----------------------!!'
    '''
    for o_f in obj_foco:
     #print 'o_f.name:',o_f.name,len(o_f.name)
     if o_f.name =='undef' or umisc.trim(o_f.name)=='':
       obj_foco.remove(o_f)
    

       

    return obj_foco


def run(lrc,ex_Data): # entry point
    return runc_layer(lrc,ex_Data)



