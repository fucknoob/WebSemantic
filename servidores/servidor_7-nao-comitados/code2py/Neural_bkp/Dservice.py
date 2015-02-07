
import umisc
import conn

conn=conn.conn_mx



def get_pages(name,usr): 
 import sys
 sys.path.append('/home/mdnetsearc/public_html/Neural/MySQLdb')
        
 import MySQLdb 
 
 def get_pgs_to_index(connect,us):
  rts=[]
  try:
   cursor = connect.cursor ()
   cursor2 = connect.cursor ()
   cursor.execute ('select url_id,sval from urlinfo where url_id not in( select just_processed from pg_processed  ) and sname = \'body\' order by url_id  LIMIT 1,5') 
   resultSet = cursor.fetchall()
   for results in resultSet:     
     id= results[0]
     pg= results[1]
     # fecha a pagina
     sql_f=" insert  into pg_processed (just_processed)  values("+str(id)+")"
     print 'Cmd-insert('+us+'):',sql_f
     cursor2.execute (sql_f) 
     rts.append([pg,str(id)])
  except Exception,err:
   print 'Error get_pages:',err  
  return rts
    
 
 #conn2= MySQLdb.connect(host='dbmy0020.whservidor.com', user='mdnetsearc' , passwd='acc159753', db='mdnetsearc')
 #rt=get_pgs_to_index(conn2,'mdnetsearc')
 #if len(rt) > 0 :
 #  return rt
 #===============================================
 conn3= MySQLdb.connect(host='dbmy0031.whservidor.com', user='esyns1' , passwd='acc159753', db='esyns1') 
 rt=get_pgs_to_index(conn3,'esyns1')
 if len(rt) > 0 :
   return rt
 #===============================================
 conn4=MySQLdb.connect(host='dbmy0025.whservidor.com', user='esyns1_1' , passwd='acc159753', db='esyns1_1') 
 rt=get_pgs_to_index(conn4,'esyns1_1')
 if len(rt) > 0 :
   return rt
 #===============================================
 conn5= MySQLdb.connect(host='dbmy0035.whservidor.com', user='esyns1_2' , passwd='acc159753', db='esyns1_2')
 rt=get_pgs_to_index(conn5,'esyns1_2')
 if len(rt) > 0 :
   return rt
 #===============================================
 #conn6= MySQLdb.connect(host='dbmy0021.whservidor.com', user='mdnetsocia' , passwd='acc159753', db='mdnetsocia') 
 #rt=get_pgs_to_index(conn6,'mdnetsocia')
 #if len(rt) > 0 :
 #  return rt
 #===============================================






def get_fuzzy(name,user):
     ''' '''
     self_name=name
     self_id=user
     affinity=self_name
     print 'Process-Lay:',affinity,self_id
     sql1="SELECT fzname,force_position,mandatory,direction,an FROM fuzzy_store  where layout_onto='"+affinity+"' and username='"+self_id+"' order by sq desc  "
     resultSet = conn.sql (sql1) 
     aresults=[]
     for results in resultSet:
        fzname=results[0]
        print 'Get-FZ:',fzname
        force_position=( umisc.trim(results[1]).upper () == "Y" or umisc.trim(results[1]).upper () == "S" )
        mandatory=( umisc.trim(results[2]).upper () == "Y" or umisc.trim(results[2]).upper () == "S" ) 
        direction=umisc.trim(results[3]).upper ()
        f_an=umisc.trim(results[4]).upper ()
        #===--------------------------------------------------
        referer=[]
        resultSet22 = conn.sql ("SELECT refer FROM fz_store_refer  where fz='"+fzname+"' and username='"+self_id+"' ")  
        for results22 in resultSet22:
          refs=results22[0]
          referer.append(refs)
        #===--------------------------------------------------
        sqlr="SELECT trim(defs),trim(sin_ret),trim(vl_ret),trim( special_direct ) FROM fz_store_defs  where fz='"+fzname+"' and username='"+self_id+"'  "
        #print sqlr
        resultSet2 = conn.sql (sqlr)
        arround=[]
        DEFS=[]
        sinap_result=[]
        for results2 in resultSet2:
          returns=[]
          vl_ret1=results2[2]
          special_direct=results2[3]
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
          for tup in tuples:             
           top=''
           sub=''
           sin=''
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
            returns.append([top,sub,sin,special_direct])
            #print returns,'...'
          #----
          defs1=results2[0]
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
          DEFS.append([ps,returns])
          sin_ret=results2[1]
          if umisc.trim(sin_ret) != '':
           sinap_result.append(sin_ret)
        #===--------------------------------------------------
        resultSet2 = conn.sql ("SELECT trim(pref) FROM  fz_store_pref  where fz='"+fzname+"' and username='"+self_id+"'  ") # 50 rows por vez
        PREF=[]
        for results2 in resultSet2:
          #----
          pref=results2[0]
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
        sqlr="SELECT trim(sufix) FROM  fz_store_sufix where fz='"+fzname+"' and username='"+self_id+"'  "
        resultSet2 = conn.sql (sqlr) # 50 rows por vez
        SUFX=[]
        for results2 in resultSet2:
          #----
          sufix=results2[0]
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
        
#c=get_fuzzy('simple-search-classificacao','igor.moraes')    

#print c


 

   