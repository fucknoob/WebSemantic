# coding: latin-1


class mdFz:
 def __init__(self,prefixo,sufixo,define,returnsa):
  self.prefixo=prefixo
  self.sufixo=sufixo
  self.define=define
  self.returns=returnsa

class mdFuzzy:
 def __init__(self):
  self.fzSent=[]
  self.name=''
 def set_fz(self,arr,c,refer,force_position,arround,snret,direction,f_an):
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
            ret.append([r[0],[r[1]],-1,self.refer,r[2]] ) 
           ret.append([self.name,[],-1,self.refer,self.sn_ret])
           #ret.append([self.name,[dt],-1,self.refer,self.sn_ret])
           return ret
          #return [[self.name,[dt],-1,self.refer,self.sn_ret]]
          return [[self.name,[],-1,self.refer,self.sn_ret]]
         else: return []
    else:  
        [r,posic]=self.compare2( dt  )
        if r :
         if self.valida_arround2(indi,dt_arr):
          #========= verificar retorno self.returns
          if len(self.fzSent) > posic :
           ret=[]
           r = self.fzSent[posic].returns
           ret.append([r[0],[r[1]],-1,self.refer,r[2]] ) 
           ret.append([self.name,[],-1,self.refer,self.sn_ret])
           #ret.append([self.name,[dt],-1,self.refer,self.sn_ret])
           return ret
          return [[self.name,[],-1,self.refer,self.sn_ret]]
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
     if ind_p > indi:
      if ind_fz < len(self.fzSent ):
       fz=self.fzSent[ind_fz]
       if self.compare(dt_arr[ind_p][0],fz) :
         ind_fz+=1
         fnd+=1
         rts.append(dt_arr[ind_p][0])
         if ind_first_fnd:
          ult_p=ind_p
         ind_first_fnd=True
         fz2.append(fz)
       elif not ind_first_fnd:
         return []        
       elif ind_first_fnd:
        if self.force_position: return[]
     ind_p+=1 
    if len(fz2) > 0:
     for fz in fz2:
         if self.valida_arround2(indi,dt_arr):
          #========= verificar retorno self.returns
          if len(fz.returns) > 0 :
           ret=[]
           for r in fz.returns:
            ret.append([r[0],[r[1]],-1,self.refer,r[2]] ) 
           ret.append([self.name,[],-1,self.refer,self.sn_ret])
           #ret.append([self.name,[dt],-1,self.refer,self.sn_ret])
           return ret       
          return [[self.name,rts,ult_p+1,self.refer,self.sn_ret]]
         else: return []
   return []
 #=====================================================   
 def process(self,dt,dt_arr,indi):
    if len(self.fzSent) <= 1 or (self.an.upper () == "OR"):
     if len(self.fzSent) <= 1:
         r=self.compare( dt  )
         if r :
          if self.valida_arround(indi,dt_arr):
           #========= verificar retorno self.returns
           if len(self.fzSent[0].returns) > 0 :
            ret=[]
            for r in self.fzSent[0].returns:
             ret.append([r[0],[r[1]],-1,self.refer,r[2]] ) 
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
            ret.append([r[0],[r[1]],-1,self.refer,r[2]] ) 
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
     while ind_p < len(dt_arr):
      if ind_p > indi:
       if ind_fz < len(self.fzSent ):
        fz=self.fzSent[ind_fz]
        if self.compare(dt_arr[ind_p],fz) :
          ind_fz+=1
          fnd+=1
          rts.append(dt_arr[ind_p])
          if ind_first_fnd:
           ult_p=ind_p
          ind_first_fnd=True
          fz2.append(fz)
        elif not ind_first_fnd:
          return []        
        elif ind_first_fnd:
         if self.force_position: return[]
      ind_p+=1 
     if len(fz2) > 0:
      for fz in fz2:
          if self.valida_arround2(indi,dt_arr):
           #========= verificar retorno self.returns
           if len(fz.returns) > 0 :
            ret=[]
            for r in fz.returns:
             ret.append([r[0],[r[1]],-1,self.refer,r[2]] ) 
            ret.append([self.name,[],-1,self.refer,self.sn_ret])
            #ret.append([self.name,[dt],-1,self.refer,self.sn_ret])
            return ret       
           return [[self.name,rts,ult_p+1,self.refer,self.sn_ret]]
          else: return []
    return []
    
 def compare(self, dt , fz=None ):
  fzs=None
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
     if dt.upper () == cmp.upper():
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
              if dt.upper () == cmp2.upper():
                return True
  return False
  

 def compare2(self, dt , fz=None ):
  indc=0
  for fzs in self.fzSent:   
   st = fzs
   prefixo=st.prefixo
   sufixo=st.sufixo
   define=st.define
   for pr in prefixo:
    cmp_=pr
    for df in define:
     cmp=cmp_+df
     if dt.upper () == cmp.upper():
       return [True,indc]
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
              if dt.upper () == cmp2.upper():
                return [True,indc]
   indc+=1             
  return [False,0]
  
    
    
    
    
  
  
  
  