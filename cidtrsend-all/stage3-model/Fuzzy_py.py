# coding: latin-1

import time, datetime
import umisc


def latinupper(string):
     return string.decode('latin-1').upper().encode('latin-1')


class mdFz:
 def __init__(self,prefixo,sufixo,define,returnsa):
  prefix=[]
  defs=[]
  sfx=[]
  #================================== 
  for p in prefixo:
   prefix.append(latinupper(p))
  #================================== 
  for d in define:
   if umisc.trim(d) != "":
    defs.append(latinupper(d))
  #================================== 
  for sf in sufixo:
   sfxc=[]
   for sf2 in sf:
    sfxc.append(latinupper(sf2))
   sfx.append(sfxc)
  #================================== 

  self.prefixo=prefix
  self.define=defs
  self.sufixo=sfx
  self.returns=returnsa

class mdFuzzy:
 def __init__(self):
  self.fzSent=[]
  self.name=''
 def set_fz(self,arr,c,refer,force_position,arround,snret,direction,f_an,breaks):
  for ar in arr:
   [prefixo,defs,sufixo]=ar
   [define,returns]= defs
   self.fzSent.append( mdFz(prefixo,sufixo,define,returns)  )
  self.mandatory=c
  self.an=f_an
  self.refer=refer
  self.arround=arround
  self.force_position=force_position
  self.sn_ret=snret
  self.direction=direction
  self.breaks=breaks
  #if self.name == 'simple-state-place':
  # for s in self.fzSent:
  #  print s.define ,'<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
  
 def valida_arround(self,idx_atu,dt_arr):
    if len(self.arround) <=0 : return True
    ind=0
    fnds=0
    ind_a=1
    tp=self.arround[0]
    if tp == '0' : # before
     for d in dt_arr:
      if ind <= idx_atu:
       if len(self.arround) > ind_a:
         id=self.arround[ind_a]
         if d.upper () == id.upper():
          fnds+=1
          ind_a+=1
      ind+=1
     if fnds >= len(self.arround)-1 :
       return True     
    if tp == '1' : # next
     for d in dt_arr:
      if ind >= idx_atu:
       if len(self.arround) > ind_a:
         id=self.arround[ind_a]
         if d.upper () == id.upper():
          fnds+=1
          ind_a+=1
      ind+=1
     if fnds >= len(self.arround)-1 :
       return True     
    return False
 def valida_arround2(self,idx_atu,dt_arr):
    if len(self.arround) <=0 : return True
    ind=0
    fnds=0
    ind_a=1
    tp=self.arround[0]
    if tp == '0' : # before
     for d in dt_arr:
      if ind <= idx_atu:
       if len(self.arround) > ind_a:
         id=self.arround[ind_a]
         if d[0].upper () == id.upper():
          fnds+=1
          ind_a+=1
      ind+=1
     if fnds >= len(self.arround)-1 :
       return True     
    if tp == '1' : # next
     for d in dt_arr:
      if ind >= idx_atu:
       if len(self.arround) > ind_a:
         id=self.arround[ind_a]
         if d[0].upper () == id.upper():
          fnds+=1
          ind_a+=1
      ind+=1
     if fnds >= len(self.arround)-1 :
       return True     
    return False
 #=====================================================
 def compare_break(self,dt):
  for b in self.breaks:
   if b==dt:
    return True
  return False
 #==
 def process2(self,dt_k,dt_arr,indi):
   dt=dt_k[0]
   if len(self.fzSent) <= 1 or (self.an.upper () == "OR"):
    if len(self.fzSent) <= 1:
        r=self.compare( dt  )
        if r :
         if self.valida_arround2(indi,dt_arr):
          #========= verificar retorno self.returns
          if len(self.fzSent[0].returns) > 0 :
           ret=[]
           for r in self.fzSent[0].returns:
            if r[1] != '$$data$$':
             ret.append([r[0],[r[1]],-1,self.refer,[r[2]]] ) 
            else:
             ret.append([r[0],[dt],-1,self.refer,[r[2]] ] ) 
           #ret.append([self.name,[],-1,self.refer,self.sn_ret])
           #ret.append([self.name,[dt],-1,self.refer,self.sn_ret])
           return ret
          #return [[self.name,[dt],-1,self.refer,self.sn_ret]]
          else: return [[self.name,[],-1,self.refer,self.sn_ret]]
         else: return []
    else:  
        [r,posic]=self.compare2( dt  )
        if r :
         if self.valida_arround2(indi,dt_arr):
          #========= verificar retorno self.returns
          if len(self.fzSent) > posic :
           ret=[]
           r = self.fzSent[posic].returns
           if r[1] != '$$data$$':
            ret.append([r[0],[r[1]],-1,self.refer,[r[2]]] ) 
           else:
            ret.append([r[0],[dt],-1,self.refer,[r[2]] ] ) 
           #ret.append([self.name,[],-1,self.refer,self.sn_ret])
           #ret.append([self.name,[dt],-1,self.refer,self.sn_ret])
           return ret
          else: return [[self.name,[],-1,self.refer,self.sn_ret]]
          #return [[self.name,[dt],-1,self.refer,self.sn_ret]]
         else: pass
        return []          
   #-------------------------    

   elif len(self.fzSent) > 1:
    ind_p=0
    ind_fz=0
    fnd=0
    rts=[]
    ult_p=-1
    fz2=[]
    ind_first_fnd=False
    while ind_p < len(dt_arr):
     if ind_p >= indi:
      if ind_fz < len(self.fzSent ):
       fz=self.fzSent[ind_fz]
       if self.compare_break(dt_arr[ind_p][0]):
        #print 'Fz.Break-1',ind_p
        break
        
       #if self.name =='simple-state-date2':
       #  print fz.returns,'>>>(2)',ind_p,'[',dt_arr[ind_p],fz,']-->',fsf
        
       if self.compare(dt_arr[ind_p][0],fz) :
         ind_fz+=1
         fnd+=1
         rts.append(dt_arr[ind_p][0])
         if ind_first_fnd:
          ult_p=ind_p
         ind_first_fnd=True
         fz2.append([fz,ind_p])
       elif not ind_first_fnd:
         return []        
       elif ind_first_fnd:
        if self.force_position: return[]
     ind_p+=1 
    #=========================
    if len(fz2) > 0:
     fc=False
     ret=[]
     has_r=False
     for [fz,ind_p2] in fz2:
          if len(fz.returns) > 0 :
            has_r=True
     #==
     for [fz,ind_p2] in fz2:
         if self.valida_arround2(indi,dt_arr):
          fc=True
          #========= verificar retorno self.returns
          if len(fz.returns) > 0 :
           for r in fz.returns:
            ret.append([r[0],[r[1]],ult_p+1,self.refer,[r[2]],ind_p2] ) 
            #print 'ss----:',self.name,':',ind_p2,(ult_p+1),r[0],r[1]
          else: 
           if not has_r:
            ret.append([self.name,rts,ult_p+1,self.refer,self.sn_ret,ind_p2])
           else:
            ret.append([self.name,rts,ult_p+1,self.refer,self.sn_ret,ind_p2,0])
        
         else: return []
     if fc : return ret    
   return []
    
   

   
 def mandatory_by_return(self,sent_ind):
  sent_f=False
  for s in self.fzSent:
   if len(s.returns) > 0:
     sent_f=True
  if not sent_f: return self.mandatory
  if len(self.fzSent) <= sent_ind:
   return False
  rts=self.fzSent[sent_ind].returns
  rtsb=False
  if len(rts) > 0 : rtsb=True
  #if self.name == 'simple-state-place': 
  # print rtsb,'>>LLLLLLLLLLLLL',sent_ind
  return rtsb
   
 #=====================================================   
 def process(self,dt,dt_arr,indi):
    #print 'Fz:.',self.name,'[',indi,']'
    if len(self.fzSent) <= 1 or (self.an.upper () == "OR"):
     if len(self.fzSent) <= 1:         
         r=self.compare( dt  )
         if r :
          if self.valida_arround(indi,dt_arr):
           #========= verificar retorno self.returns
           if len(self.fzSent[0].returns) > 0 :
            ret=[]
            for r in self.fzSent[0].returns:
             r3=None
             if len( r ) > 3:
              r3=r[3]
             #print r , '<<<<<<<<<<<<<<<<<<<<<<(1)'             
             if r[1] != '$$data$$':
              ret.append([r[0],[r[1]],-1,self.refer,[r[2]],-1,r3] ) 
             else :
              ret.append([r[0],[dt],-1,self.refer,[r[2]],-1,r3 ] ) 
            ret.append([self.name,[],-1,self.refer,self.sn_ret])
            #ret.append([self.name,[dt],-1,self.refer,self.sn_ret])
            return ret
           #return [[self.name,[dt],-1,self.refer,self.sn_ret]]
           return [[self.name,[],-1,self.refer,self.sn_ret]]
          else: return []
     else:  
         [r,posic]=self.compare2( dt  )
         if r :
          if self.valida_arround(indi,dt_arr):
           #========= verificar retorno self.returns
           if len(self.fzSent) > posic :
            ret=[]
            r = self.fzSent[posic].returns
            #if len(self.fzSent[posic].returns)>0:
            # print 'FZ-RTS:',self.fzSent[0].returns
            #print r , '<<<<<<<<<<<<<<<<<<<<<<(2)'            
            for r1 in r:
             r3=None
             if len( r1) > 3:
              r3=r1[3]
             if r1[1] != '$$data$$':
              ret.append([r1[0],[r1[1]],-1,self.refer,[r1[2]],-1,r3] ) 
             else: 
              ret.append([r1[0],[dt],-1,self.refer,[r1[2]],-1,r3 ] ) 
            #ret.append([self.name,[dt],-1,self.refer,self.sn_ret])
            ret.append([self.name,[],-1,self.refer,self.sn_ret])
            return ret
           #return [[self.name,[dt],-1,self.refer,self.sn_ret]]
           return [[self.name,[],-1,self.refer,self.sn_ret]]
          else: pass
         return []          
    #-------------------------      
    elif len(self.fzSent) > 1:
     ind_p=0
     ind_fz=0
     fnd=0
     rts=[]
     ult_p=-1
     fz2=[]
     ind_first_fnd=False
     deb_break=False
     while ind_p < len(dt_arr):
      if ind_p >= indi:
       if ind_fz < len(self.fzSent ):
        fz=self.fzSent[ind_fz]
        if self.compare_break(dt_arr[ind_p]):
         #print 'Fz.Break-2:',ind_p
         deb_break=True
         break     
        fsf=self.compare(dt_arr[ind_p],fz)
        #print 'Comps: ---- ',dt_arr[ind_p],fz,fsf
        #if self.name =='simple-state-place':
        # print fz.returns,'>>>(1)',ind_p,'[',dt_arr[ind_p],fz.define,']-->',fsf
        if fsf :
          ind_fz+=1
          fnd+=1
          rts.append(dt_arr[ind_p])
          if ind_first_fnd:
           ult_p=ind_p
          ind_first_fnd=True
          fz2.append([fz,ind_p,dt_arr[ind_p]])
        elif not ind_first_fnd:
          #print 'End:------------(C)','[',ind_p,']'
          return []        
        elif ind_first_fnd:
         if self.force_position: 
          #print 'End:------------(D)','[',ind_p,']'
          return[]
      ind_p+=1       
     #if len(fz2) > 0:
     #if self.name =='simple-class-collect2':
     # print len(fz2),len(self.fzSent),'<<<<<<<<<<<<<<<<<<',fz2
     #if self.name == 'simple-collect-inferencia-preditiva':
     # print fz2,'!!!!'
     #print 'Found:',len(fz2),len(self.fzSent)
     if len(fz2) >=  len(self.fzSent):
      fc=False
      ret=[]
      for [fz,ind_p2,dt_atu] in fz2:
          #if self.name == 'simple-collect-inferencia-preditiva':
          #  print [fz,ind_p2],'!!!!'
          #==
          if self.valida_arround2(indi,dt_arr):
           fc=True
           #========= verificar retorno self.returns
           #if self.name =='simple-collect-inferencia-preditiva':
           #  print ind_p2,fz.returns,'<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
           if len(fz.returns) > 0 :
            for r in fz.returns:
             #print r , '<<<<<<<<<<<<<<<<<<<<<<(3)' 
             r3=None
             if len(r) >3:
              r3=r[3]      
             #if self.name == 'simple-state-place': 
             # print 'R:',r,'->',dt_atu             
             if r[1] != '$$data$$':
              ret.append([r[0],[r[1]],ult_p+1,self.refer,[r[2]],ind_p2,r3] ) 
             else: 
              ret.append([r[0],[dt_atu],ult_p+1,self.refer,[r[2]],ind_p2,r3] ) 
            
           else: ret.append( [ self.name,[],ult_p+1,self.refer,self.sn_ret,ind_p2,'' ] )
          else: return []
      #if self.name =='simple-state-place':
      # print 'FZ>Found:',fc,ind_p2,ret
      if fc: 
       #print ret,'===================================='
       return ret    
    return []
    
    
    
 def compare_Date_del(self,t_format,dt):
    #timestring = "2005-09-01 12:30:09"
    #time_format = "%Y-%m-%d %H:%M:%S"
    #datetime.datetime.fromtimestamp(time.mktime(time.strptime(mytime, time_format)))
    rt=False
    try:
     r=datetime.datetime.fromtimestamp(time.mktime(time.strptime(dt, t_format)))
     return True
    except:
     pass
    return False
  
   
 def compare_data_h(self,dt1,dt2):
   d1=dt1
   d2=dt2
   if d1.lower() == '#month':
     if d2.lower() in ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']:
       return True
   #===================
   if d1.lower() == '#day':
    try:
     if int(d2) in  [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,28,30,31]:
       return True     
    except: 
      pass
   #==   
   if d1.lower() == '#year':
    try:
      if int(d2) > 0 :
        return True
    except Exception,e:
     #print 'Err:Year:',e
     pass     
   #=========================  
   if d1.lower() == '#time':
    try:
      #def compare_Date_del(self,t_format,dt):
      #  timestring = "2005-09-01 12:30:09"
      #  time_format = "%Y-%m-%d %H:%M:%S"
      if self.compare_Date_del('%H:%M:%S',d2) :
        return True
    except:
     pass
   #=========================  
   if d1.lower() == '#date':
    try:
      #def compare_Date_del(self,t_format,dt):
      #  timestring = "2005-09-01 12:30:09"
      #  time_format = "%Y-%m-%d %H:%M:%S"
      if self.compare_Date_del('%Y-%m-%d',d2) :
        return True
    except:
     pass
   if d1.lower() == '#datetime':
    try:
      #def compare_Date_del(self,t_format,dt):
      #  timestring = "2005-09-01 12:30:09"
      #  time_format = "%Y-%m-%d %H:%M:%S"
      if self.compare_Date_del('%Y-%m-%d %H:%M:%S',d2) :
        return True
    except:
     pass
    #======================================= 
    return False   


 #import mdFuzzy    
    
 def compare(self, dt , fz=None ):
  fzs=None
  dt=latinupper(dt)
  if fz :
   fzs=fz 
  elif len(self.fzSent) > 0:
   fzs=self.fzSent[0]   
  if True:
   st = fzs
   prefixo=st.prefixo
   sufixo=st.sufixo
   define=st.define
   returns=st.returns
   for pr in prefixo:
    cmp_=pr
    for df in define:
     cmp=cmp_+df
     
         
     if self.compare_data_h(cmp,dt):
      #print 'cmp-dt(1):',cmp,dt
      return  True
     
     #cmp=latinupper(cmp)
     # conferir #data, #year, #month, #dia , #hora
     #if (cmp).lower() == '$$all$$': # $$all$$
     #  print 'kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk'

     rs=(dt  == cmp or (cmp).lower()  == '$$all$$')
     
     #if self.name =='simple-state-place':
     #    print '((1)):',cmp, dt ,'>>>',rs   

     
     if rs:
       return True
     #=============
     is1=0
     while  len(sufixo) > is1:      
       sufd=sufixo[is1]
       is1+=1
       for sufd2 in sufd:
         is2=0
         while len(sufixo)> is2:  
           suf= sufixo[is2]
           is2+=1          
           if is2 > is1 : 
             for suf2 in suf:          
              cmp2=cmp+sufd2+suf2
              #cmp2=latinupper(cmp2)
              if dt  == cmp2 :
                return True
  return False
  
     
 def compare2(self, dt , fz=None ):
  indc=0
  dt=latinupper(dt)
  for fzs in self.fzSent:   
   st = fzs
   prefixo=st.prefixo
   sufixo=st.sufixo
   define=st.define
   for pr in prefixo:
    cmp_=pr
    for df in define:
     cmp=cmp_+df
     #cmp=latinupper(cmp)
     #if (cmp).lower() == '$$all$$':
     #  print 'kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk'
     
     if dt == cmp or (cmp).lower()  == '$$all$$':
       return [True,indc]
     #=====================  
     if self.compare_data_h(cmp,dt):
      #print 'cmp-dt(2):',cmp,dt
      return  [True,indc]
       
     #=============
     is1=0
     while  len(sufixo) > is1:      
       sufd=sufixo[is1]
       is1+=1
       for sufd2 in sufd:
         is2=0
         while len(sufixo)> is2:  
           suf= sufixo[is2]
           is2+=1          
           if is2 > is1 : 
             for suf2 in suf:          
              cmp2=cmp+sufd2+suf2
              #cmp2=latinupper(cmp2)
              if dt  == cmp2 :
                return [True,indc]
   indc+=1             
  return [False,0]
  
    
    
    
    
  
  
  
  