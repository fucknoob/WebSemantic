
import umisc

import pycassa
from pycassa.pool import ConnectionPool
from pycassa import index
from pycassa.columnfamily import ColumnFamily 


pool2 = None
tb_fuzzy = None
tb_fz_store_pref=None
tb_fz_store_defs=None
tb_fz_store_sufix=None
tb_fz_store_refer=None
tb_fz_arround_points=None


def init_base():
 global pool2
 global tb_fuzzy
 global tb_fz_store_pref
 global tb_fz_store_defs
 global tb_fz_store_sufix
 global tb_fz_store_refer
 global tb_fz_arround_points
 #
 pool2 = ConnectionPool('MINDNET', ['79.143.185.3:9160'],timeout=10000)
 tb_fuzzy = pycassa.ColumnFamily(pool2, 'fuzzy_store') 
 tb_fz_store_pref=pycassa.ColumnFamily(pool2,"fz_store_pref")
 tb_fz_store_defs=pycassa.ColumnFamily(pool2,"fz_store_defs")
 tb_fz_store_sufix=pycassa.ColumnFamily(pool2,"fz_store_sufix")
 tb_fz_store_refer=pycassa.ColumnFamily(pool2,"fz_store_refer")
 tb_fz_arround_points=pycassa.ColumnFamily(pool2,"fz_arround_points")


from operator import itemgetter, attrgetter
 
def get_fuzzy2(name,user):
     ''' '''
     affinity=name
     #==
     cl4 = index.create_index_expression(column_name='layout_onto', value=affinity)
     clausec = index.create_index_clause([cl4],count=1000000)
     resultSet2=tb_fuzzy.get_indexed_slices(clausec) 
     resultSet=[]
     aresults=[]
     for ky,re in resultSet2:
         # 
         fzname=re[u'fzname']
         force_position=re[u'force_position']
         mandatory=re[u'mandatory']
         direction=re[u'direction']
         an=re[u'an']
         sq=int(re[u'sq'])
         resultSet.append([ ky,fzname,force_position,mandatory,direction,an,sq  ])
     #
     #
     resultSet=sorted(resultSet, key=itemgetter(6), reverse=True)      
     #
     for results in resultSet:
        [ky,fzname,force_position,mandatory,direction,an,sq]=results
        #print 'Get-FZ:',fzname
        force_position=( umisc.trim(force_position).upper () == "Y" or umisc.trim(force_position).upper () == "S" )
        mandatory=( umisc.trim(mandatory).upper () == "Y" or umisc.trim(mandatory).upper () == "S" ) 
        direction=umisc.trim(direction).upper ()
        f_an=umisc.trim(an).upper ()
        #===--------------------------------------------------
        referer=[]
        start_i=0
        while True:
           start_i+=1
           try:  
            r1=tb_fz_store_refer.get(fzname+"|"+str(start_i))
           except: 
                break
           referer.append(r1[u'refer'])
           
        #===--------------------------------------------------
        #sqlr="SELECT trim(defs),trim(sin_ret),trim(vl_ret),trim( special_direct ) FROM fz_store_defs  where fz='"+fzname+"' and username='"+self.id+"'  "
        #print sqlr
        has_break=False
        breaks=[]
        arround=[]
        DEFS=[]
        sinap_result=[]
        start_i=0
        while True:
          start_i+=1 
          try:
             results2=tb_fz_store_defs.get(fzname+"|"+str(start_i))  
          except:
            break   
          returns=[]
          vl_ret1=results2[u'vl_ret']
          special_direct=results2[u'special_direct']
          if special_direct == None: special_direct=''
          if vl_ret1 == None: vl_ret1=''
          # formato : [ topico,sub,sinapse ][topico,sub,sinapse][topico,sub,sinapse]
          tuples=[]
          tmp=''
          for s in vl_ret1:
           if s == '[':
            tmp=''
           elif s == ']':
            tuples.append(tmp)
            tmp=''
           else:
             tmp+=s
          #print 'tuples:',tuples   
          for tup in tuples:             
           top=''
           sub=''
           sin=''
           tmp=''
           for s in tup:
             if s == ',':
              if top == '':
                top=tmp
                tmp=''
              elif sub == '':
                sub=tmp
                tmp=''
              else:
                sin=tmp
                tmp=''
             else: tmp+=s   
           if umisc.trim(tmp) != '' :
              sin=tmp
           if umisc.trim(top) != '':
            if top == 'break':
             has_break=True
            else: 
             returns.append([top,sub,sin,special_direct])
          #print returns,'...'
          #----
          defs1=results2[u'defs']
          ps=[]
          if len(defs1) > 0 :
           tmp=''
           ind=0
           for d in defs1:
            if d == ',' :
             if defs1[ind-1] != '\\' :
               ps.append(tmp)
               tmp=''
             elif d != '\\' : tmp+=d            
            elif d != '\\' : tmp+=d
            ind+=1
           if umisc.trim(tmp) != '': ps.append(tmp) 
          else:
           ps.append('')
          if has_break:
           for ss in ps:
            breaks.append(ss)
          else:
           DEFS.append([ps,returns])
           sin_ret=results2[u'sin_ret']
           if umisc.trim(sin_ret) != '':
            sinap_result.append(sin_ret)
        #===--------------------------------------------------
        #
        # 
        PREF=[]
        start_i=0
        while True:
          start_i+=1
          try:  
            r1=tb_fz_store_pref.get(fzname+"|"+str(start_i))
          except: 
                break
          pref=r1[u'pref']
          ps=[]
          if len(pref) > 0 :
           tmp=''
           ind=0
           for d in pref:
            if d == ',' :
             if pref[ind-1] != '\\' :
               ps.append(tmp)
               tmp=''
             else : tmp+=d
            else: tmp+=d
           if tmp != '' : ps.append(tmp) 
          else:
           ps.append('')
          PREF.append(ps)
        
        #===--------------------------------------------------
        #sqlr="SELECT trim(sufix) FROM  fz_store_sufix where fz='"+fzname+"' and username='"+self.id+"'  "
        #
        SUFX=[]
        start_i=0
        while True:
          start_i+=1
          try:  
            r1=tb_fz_store_sufix.get(fzname+"|"+str(start_i))
          except: 
                break
          sufix=r1[u'sufix']
          ps=[]
          if len(sufix) > 0 :
           tmp=''
           ind=0
           for d in sufix:
            if d == ',' :
             if sufix[ind-1] != '\\' :
               ps.append(tmp)
               tmp=''
             else : tmp+=d
            else: tmp+=d
           if tmp != '' :  ps.append(tmp) 
          else:
           ps.append('')          
          SUFX.append(ps)
        #===--------------------------------------------------        
        ind =0
        sents=[]
        for cDF in DEFS:
         PR=['']
         SF=[['']]
         if ind < len(PREF):
          PR=PREF[ind]
         if ind < len(SUFX): 
          SF=SUFX
         DEF=cDF
         sent=[PR,DEF,SF]
         sents.append(sent)
         ind+=1
        aresults.append( [fzname,sents,mandatory,referer,force_position,arround,sinap_result,direction,f_an] )
                                       
     return aresults
           
      
cache=[] 

init_base()

def get_fuzzy(name,user):
 global cache
 ind=0
 for [nm,cont,used] in cache:
  if nm == name and used < 1000000: # atualizar a cada 1.000.000 usos
    cache[ind][2]=cache[ind][2]+1 
    return cont
  ind+=1  
 rt=get_fuzzy2(name,user) 
 cache.append([name,rt,0]) 
 return rt

 
 
 
 
 

   