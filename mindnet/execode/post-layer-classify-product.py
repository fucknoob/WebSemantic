#EXEC
import mdNeural
import umisc
import string

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
    not_in=['alias','object3','class','indicator','defin','simple-collect','sample','equilibrio','know','mean','qtd-','time','indicative','interact','state','accept','way','need','intensity','grow','order','simple-','value','enum','event','news','referencial','compare','number']
    # Relaction-oper-opcode opcode original dos qualificadores se nao especificado
    #=====================================================
    def get_o_ob():
        for s in objects:
            if s.name==ob: return s
        return None
    #=====================================================
    class_fnd=False
    if True:
       print 'RTS(1-S.2):------------','[',ex_Data,']'
       r=layer
       for s in r.topicos:
         for kdata in s.dt:
            if  kdata.lower().startswith('defs') or kdata.lower().startswith('interact.') :
             class_fnd=True
             break
         if 'category' in s.dt or 'class' in s.dt :
          class_fnd=True
         if 'object' in s.dt:
          for ds in s.sinapses:
           if 'category' in ds.nr.dt or 'defs' in ds.nr.dt :
            class_fnd=True

         print 'Topico:',s.dt
         #====================================================
         tp=s
         if 'object' in tp.dt :
          sn_dt=''
          lst=[]
          print 'obj.alias.snp:',tp.sinapses
          has_spaced=False
          analiz=[]
          for skl1 in tp.sinapses:
           for dp in skl1.nr.dt:
            analiz.append(dp)
            if umisc.trim(dp)!='' and umisc.trim(dp)!='\n' and umisc.trim(dp) != 'start' and umisc.trim(dp) != '.':
               has_spaced=True
          print 'has_spaced:',has_spaced,analiz
          if len(tp.sinapses) == 0 or (not has_spaced  ):
            for d in ex_Data:
             sn_dt=ex_Data[0]
            sn_dt=sn_dt.replace('\n','')
            sn_dt=sn_dt.replace('\t','')
            sn_dt=sn_dt.replace('.',' ')
            #sn_dt = filter(lambda x: x in string.printable, sn_dt)
          for sn in tp.sinapses:
           for a in sn.nr.dt:
            if a.lower() == 'start' or a.lower() == 'end' :
               tp.sinapses.remove(sn)
               break

          for sn in tp.sinapses:
           ah=False
           for a in sn.nr.dt:
            for cin in not_in:
             if cin in a.lower() and a.lower() != 'evento' and a.lower() != 'eventos' and (not a.lower().startswith('interact.' )) :
              ah=True
              continue
            sn_dt=umisc.trim(sn_dt)+(' '+a+' ' )
           if ah:
            lst.append(sn.nr)
            continue

          sn_dt=umisc.trim(sn_dt)
          print 'Collect layer.sn_dt:',sn_dt
          if umisc.trim(sn_dt) != '$$id$$' and umisc.trim(sn_dt) != '':
           new_k=sn_dt
           if umisc.trim(new_k) not in ex_Data:
            ex_Data.append(umisc.trim(new_k))
            print 'ex:data:',ex_Data
         #====================================================
         print 'SNS:------------------------------------------'
         for s1 in s.sinapses:
           print '           ',s1.nr.dt
           for s2 in s1.nr.sinapses:
             print '                        ',s2.nr.dt
             for s3 in s2.nr.sinapses:
               print '                                  ',s3.nr.dt
         print '----------------------------------------------'
       print 'RTS(1-S.2)(END):------------'
    #===============================
    print 'need_fnd(2):',class_fnd
    if not class_fnd:
     return
    obj_foco=[]
    ex_Data2=[]
    #=
    #print 'N tops:' , len(layer.topicos)
    found_obj_1=False
    first_t=True
    print 'dump.layer:',layer.name
    layer.dump_layer()
    for t in layer.topicos:
        tp=t
        nr_t=t.dt[0]
        nr_t=nr_t.replace('\n','')
        if umisc.trim(nr_t) == '' or umisc.trim(nr_t) == '\n' : continue
        #======================================
        if 'object' in t.dt :
         sn_dt=''
         lst=[]
         print 'obj.alias.snp:',tp.sinapses
         has_spaced=False
         analiz=[]
         for skl1 in tp.sinapses:
           for dp in skl1.nr.dt:
            analiz.append(dp)
            if umisc.trim(dp)!='' and umisc.trim(dp)!='\n' and umisc.trim(dp) != 'start' and umisc.trim(dp) != '.':
               has_spaced=True
         print 'has_spaced:',has_spaced,analiz
         if len(tp.sinapses) == 0 or (not has_spaced  ):
           for d in ex_Data:
            sn_dt=ex_Data[0]
           sn_dt=sn_dt.replace('\t','')
           sn_dt=sn_dt.replace('\n','')
           sn_dt=sn_dt.replace('.',' ')
           #sn_dt = filter(lambda x: x in string.printable, sn_dt)
         for sn in tp.sinapses:
          ah=False
          for a in sn.nr.dt:
           if (a.lower().startswith('interact.' )):
            lst.append(sn.nr)
            continue
           for cin in not_in:
            if cin in a.lower() and a.lower() != 'evento' and a.lower() != 'eventos' and a.lower() != 'start' and a.lower() != 'end' :
             ah=True
             continue
           sn_dt=umisc.trim(sn_dt)+(' '+a+' ' )
          if ah:
           lst.append(sn.nr)
           continue

         sn_dt=umisc.trim(sn_dt)
         print 'Collect layer.sn_dt(2):',sn_dt
         if umisc.trim(sn_dt) != '$$id$$' and umisc.trim(sn_dt) != '':
          lay=mdNeural.mdLayer()

          new_k=sn_dt
          if umisc.trim(new_k) not in ex_Data:
           ex_Data.append(umisc.trim(new_k))
           print 'ex:data:',ex_Data
          lay.name= umisc.trim(new_k)

          if umisc.trim(sn_dt) == '':
           if len(ex_Data) > 0   :
             print 'ex_Data(1)-->',ex_Data
             for s in ex_Data:
              if umisc.trim(s.name) == '':
               lay.name = s.name
               break


          for topico_rsfd in lst:
           lay.set_topico_nr(topico_rsfd)
          #====
          #print 'lay-name:',lay.name
          objects.append(lay)

          # verificar se tem mais de 3 words no nome do objeto, restringir ate achar ['o','a']
          #lay.name=sep_multiple_data_unkwon(lay.name)

          print 'Collect layer(2):',lay.name

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


    for o_f in obj_foco:
     #print 'o_f.name:',o_f.name,len(o_f.name)
     if o_f.name =='undef' or umisc.trim(o_f.name)=='':
       obj_foco.remove(o_f)



    print 'OBS.return:',len(obj_foco)
    return obj_foco


def run(lrc,ex_Data): # entry point
    return runc_layer(lrc,ex_Data)



