
import os
import sys
import time
import simplejson
import urllib
import urllib2
import umisc
import gc
import thread
import time
import logging


sys.path.append('./pycassa')
 
 

import pycassa
from pycassa.pool import ConnectionPool
from pycassa import index
from pycassa.columnfamily import ColumnFamily
 
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('GET-FACEBOOK->COLLECT')


pool2 = ConnectionPool('MINDNET', ['91.205.172.85:9160'],timeout=10000)
 


to_reopen = pycassa.ColumnFamily(pool2, 'to_reopen')
fcb = pycassa.ColumnFamily(pool2, 'fcb_users')
web = pycassa.ColumnFamily(pool2, 'web_cache')

import threading

lock = threading.Lock()



def insere_usr(user_name,idc,u_name): 
 with lock:
  try:
   ky=str(idc)
   try:
    rt=fcb.get(ky)
    pass
   except:    
    fcb.insert(ky , {'user_name':  user_name ,'id':ky , 'u_name':u_name,'indexed':'N'})
  except Exception,e: 
    print 'Error:post.usr:',e
     
  
def post_termo(it,termo,purpose,user,prep):
 with lock:
  print 'post text:',len(it)
  try:
     for its in it:
         [ from_msg,msg_id,msg_story,msg_caption,msg_description,msg_picture,msg_link,msg_name,msg_icon,msg_type,msg_likes,msg_message ]=its 
         
         if msg_message== None: msg_message=''
         if msg_caption== None: msg_caption=''
         if msg_description== None: msg_description=''
         if msg_name== None: msg_name=''
         if msg_story== None: msg_story=''
         if msg_picture== None: msg_picture=''
         if msg_link== None: msg_link=''
         if msg_icon== None: msg_icon=''
         if msg_type== None: msg_type=''
         if len(from_msg) == 0: from_msg.append(['0',msg_name])
         
         
         try:  
          msg_caption=msg_caption.encode('latin-1','ignore')   
         except : pass

         try:  
          m1=msg_name.encode('latin-1','ignore')
         except Exception,err : print 'Erro msg_caption(1):',err,msg_caption,msg_name

         try:  
          msg_caption=msg_caption+' '+m1
         except Exception,err : print 'Erro msg_caption(2):',err,msg_caption,msg_name
         

         try:  
          msg_link=msg_link.encode('latin-1','ignore')   
         except : pass
         try:  
          msg_message=msg_message.encode('latin-1','ignore')   
         except : pass
         try:  
          msg_description=msg_description.encode('latin-1','ignore')   
         except : pass
         try:  
          msg_icon=msg_icon.encode('latin-1','ignore')   
         except : pass
         try:  
          msg_picture=msg_picture.encode('latin-1','ignore')   
         except : pass
         try:  
          msg_story=msg_story.encode('latin-1','ignore')   
         except : pass
         try:  
          msg_type=msg_type.encode('latin-1','ignore')   
         except : pass
         try:  
          from_msg[1]=from_msg[1].encode('latin-1','ignore')
         except : pass
         try:  
          msg_id=msg_id.encode('latin-1','ignore')
         except : pass
         
          
         
         msg_link=msg_link.replace('\n','')
         msg_icon=msg_icon.replace('\n','')
         msg_picture=msg_picture.replace('\n','')
         msg_story=msg_story.replace('\n','')
         msg_caption=msg_caption.replace('\n','')
         msg_message=msg_message.replace('\n','')
         msg_description=msg_description.replace('\n','')
          
         msg_link=msg_link.replace('\\n','')
         msg_message=msg_message.replace('\\n','')
         msg_description=msg_description.replace('\\n','')
         msg_icon=msg_icon.replace('\\n','')
         msg_picture=msg_picture.replace('\\n','')
         msg_story=msg_story.replace('\\n','')
         msg_caption=msg_caption.replace('\\n','')
         
         all_msg=msg_message +' '+msg_description 
         
         if msg_type == u'status':
          all_msg=msg_story 
          msg_link='{owner}'      
         
         
         if umisc.trim(all_msg) <> '' or umisc.trim(msg_caption) <> '': 
          if umisc.trim(msg_link) == '' : msg_link='-'
          if umisc.trim(all_msg) == '': all_msg='-'
          if umisc.trim(termo) == '' : termo='-'
          if umisc.trim(user) == '' : user='-'
          if umisc.trim(purpose) == '' :purpose ='-'
          if umisc.trim(msg_icon) == '' :msg_icon ='-'
          if umisc.trim(msg_picture) == '' : msg_picture='-'
          if umisc.trim(from_msg[0]) == '' : from_msg[0]='0'
          if umisc.trim(from_msg[1]) == '' :from_msg[1] ='-'
          if umisc.trim(msg_story) == '' :msg_story ='-'
          if umisc.trim(msg_type) == '' : msg_type='-'
          from_msg=(from_msg)
          if umisc.trim(msg_id) == '' : msg_id='-'
          # 
          try:   
           web.insert(str(msg_id) , {'url':msg_link,'pg':all_msg ,'termo':termo,'usr':user,'purpose':purpose,'processed':'N','url_icon':msg_icon,\
                                  'url_picture':msg_picture,'id_usr':str(from_msg),'name_usr':'','story':msg_story,'title':msg_caption,\
                                  'doc_id':msg_id,'tp':msg_type,'tps':'F','indexed':'N'})
          except Exception,err:
           log.exception("Error post facebook item:")          
         else:
          pass 
  except:
   log.exception("")
  print 'post.term OK.' 
 
 
 
 
tokens=[]

il=0
while il < 90:
 tokens.append(None)
 il+=1

tokens[89]='342297925890698|e8Z0sfEk4C1QsRYddnhYGiTMBBE'
tokens[88]='639867876042862|sIOhiJ4LQa5wBF_Nsk3uv7-90q0' 
tokens[87]='140059119498348|26E21CWhzZYZf83C-qxV-Oi3tZY'
tokens[86]='439176372831254|wEa_7AybPE9LA8Ny1S9bUznW2OQ'
tokens[85]='524349027607967|1x1ocnJ1NYsLx3-2O9qfg8pK5nA'
tokens[84]='423769027708087|-eq_2e7SHcdJV44fLSGVcpRx5Io'
tokens[83]='341124109325115|D9dUjIgIYWWlcSngpj3Ty6DB7Yo'
tokens[82]='487822007944103|c6v_4IHRtx8ZWFrZ2XtDfEGKwgw'
 
 
tokens[81]='510890778954407|Mq-lVV-PgqELOnr80pGBxuDTdP4'
tokens[80]='488406387879768|MNihz851BPbaCZlUE9vF30cqDYE'
tokens[79]='379675202140272|Es8zkMcTDAMz4d2McnMOkQ0kbBQ'
tokens[78]='222192207925341|B-Ze8SZUiGnhMnghCiAATZwb6w8'
tokens[77]='162320250591840|6jndicQDj8YgHfga3NJxfqv2KEE'
tokens[76]='562214360463921|GKdbZIoE3q9T8fi4LhAcqo4DvM0'
tokens[75]='521515587887188|v88hLEgtdHTCFfIWLdTcPgN7O7Q'
tokens[74]='143154009185550|SlwteC33mTO27I202kWb6Ip2_1g'
tokens[73]='128846493962473|mKUfk9dB5nT0bueKlMdWap-RlBk'  
tokens[72]='436475979759857|y5uRJqX23I4fK0cChHXysiJyVHk'
tokens[71]='152163471610315|jnUlhQDe-BvredXvNLlncxg6ySg'
tokens[70]='430622980354937|WdkF7tShNE89noQUsTOJUhWa93g'
tokens[69]='132853053558777|UEbBzbJTt4dg8AbPkzPV4XrJ0qw'
tokens[68]='471850762868813|0FHgE5PI3lDrWLZKDEI3jcXu9eE'
tokens[67]='546489328717886|vT6oTkyJ2MI4_wUPAceTsfL-WzY'
tokens[66]='172583849555937|vAxNQPm-WqT4i8tJh8dfR7vjDa4' 
 
tokens[65]='221797974633657|Sf2e-5RkC2N9Put5mmsBBqEE-3Q' 
tokens[64]='449426581794285|2aLlKzKu9RBYkyltdwO3PMKSbx0' 
tokens[63]='100192456837036|LwGzWpDGbfci0G2Eq1BfJXDhf38'
tokens[62]='137090663127475|NSY7njMNLux97Fso9rTtuBWh98A'
tokens[61]='513270582057701|Eg3W6VwNWekY8JUTmXR0LowMRAw'
tokens[60]='188986434558866|0cX6fmPBqwcTm5meVQOLoao4YN8' 
tokens[59]='226497987491232|5QT9Ol0rOL7x0vG-VGMhwtwBMhc'
tokens[58]='497647106959190|MXwBwCHvik7GE443LxdfIO__pFU' 
tokens[57]='348124345296976|8wLxoUjp4XZKq-ujCLfmIrkYnxU'
tokens[56]='517260394990855|MtKYfICOnm1qlkiZXc18OWsslBA'
tokens[55]='430015123749909|phpz6JPQNgx-xtunkGsYtEw9bCc'
tokens[54]='563464453678457|8J-uUesGtHv61uyO9YVp8TlhGhw'
tokens[53]='529400947082887|a47I9Ox2pb1gp3yimc5We9yb-OU'
tokens[52]='574348549245088|ckCzVR62UsBFMa2aGkMxP1AyN-k'
tokens[51]='477037512352239|2ko1Uep--NfoAweRgKLAN98rhpY'
tokens[50]='483252228402257|c-jz36w8rzUHNynFRCXiigtDxfI' 
tokens[49]='613263715357067|whR-T9hvC0pScgvF65ab_xt4AfQ'
tokens[48]='107852799384937|T2dBPx3kk9dK57ouaKGS3vNU0D8' 
tokens[47]='347211275389960|NXLD3FRy8tf2YultTHPoBPOeFl0'
tokens[46]='577927638897780|fYvhaKypiSbXxam0y0CXx6c_UEc'
tokens[45]='536558349717506|xU2rZ_EzqSE53xq5dvGpL88u7V4'
tokens[44]='152412961583468|kKMxouvq8qkQoDdw7NjNRP7vejo'
tokens[43]='422989071120755|FJm5PDaa8pEP0yUN7WE7caHWw-o'
tokens[42]='421686171255791|cRfU4HDywrtKKMLKHFgV1EQzbdk'
tokens[41]='144859379009432|fbaedrRChCEiBWExmr23vhRnnLo'
tokens[40]='558766304143182|Tu24ejaTo7jsmpqVcwX0nmouI1U'
tokens[39]='368418229932570|1Ek-ggqo_HIwWPcseFfwcLI0ukk'
tokens[38]='440275279381398|-RHdmpja84V2kaCvpUJ2-Luhn_8'
tokens[37]='479203372147163|lxKHOmZTUNxTUBK8mSVOYmGBMeE'
tokens[36]='532386043448780|uAdTF4klJOOzRnTQMPB8S1fEp0s'
tokens[35]='540596275971818|WGOG4-77i74NWOQb-OUTeG0Nn00'
tokens[34]='212689678876756|GmBL2JYpgnOqAzgKJm-ecwdzNRQ'
tokens[33]='241451205992188|MHE80Q5ApflqsRZwdtrKBd_NN8o'
tokens[32]='292027807593736|g-6pg7OWcur42CMFyD5Hyb6-ZHQ'
tokens[31]='538633296167886|Bdw7ymFW2NHOtv_huREajRjQbPU'
tokens[30]='433881890025808|D0kdJd0o03BHJCCDyaB4O_3U80s'
tokens[29]='486585281405838|FFHzDMWT3IZqN2hgrYtTJCGbblU'
tokens[28]='335042546597100|nTnzeNDaUxNpdQjj_lpWZu1hSOw'
tokens[27]='527929807251380|W7y9NLHiE4bzrORyURp9SFdgImA'
tokens[26]='159391570881637|yzA1-eLm7kbL4wi4bowfvx_z7tk'
tokens[25]='343587332418941|EfnHPh32gf1rHXq5up6Oswtenk0'
tokens[24]='121461448035692|4z3bZJHFimUjOImCo5WNU8rSpOc'
tokens[23]='541445592554265|i-n8DHQIHj6M_R2qYw2znst77gY'
tokens[22]='445431948858991|9emS_RNnTT-7AtKjb5Jp-gQZhOI'
tokens[21]='412021278891698|TEx-GbUJtfC_kZXjko_60dFax2w'
tokens[20]='344164322356768|D6GiezoepN2lfX3vsKbrk9bIQ9g'
tokens[19]='431046983630836|KudqynGWcVEYE2uzvcfHxflhwvI'
tokens[18]='488000317928047|j-Bi7DvIxP0MK4vkC-QDStH94sg'
tokens[17]='140340406129503|H-KmDtTR0gGy_vzPSHttzxgRS6k'
tokens[16]='338624246246319|-Dz-etLgJsEHiUihA4f9tAJBcQk'
tokens[15]='430951943650688|ZhUkw8DNJxhPnHVvGZ_GUiWVMDk'
tokens[14]='333625310075436|mFLhsN4JXIRHdhNrs2WBjl8UBc8'
tokens[13]='333862646714535|oGpuv_fwa74hQAOWEW8cJeTqZww'
tokens[12]='123277254516880|0UtUhYxFzfOhqaUQ6ryoG0NiGeA'
tokens[11]='326490144129558|FAGR3TiWLerriH_XUIHkQMJcpo8'
tokens[10]='426035490806918|vJftgwMhcHpY3wFVjjNcVZvwM7k' 
tokens[9]='386459591441254|A5t_SUmvz8icX_KZZ4VmxAulrBU'      
tokens[8]='133520460140565|sQ86q65pby1ek6CCngarywU51nA'      
tokens[7]='130476403781113|JnKbEIwbD6c7YL0lXMAaRZSbmdk'      
tokens[6]='210200879116690|l8ZTuij9batvtjScFqr9s_WQIxE'      
tokens[5]='130873000405995|5N0XoPtYqnfP0LBj8g-oeIO90MI'    
tokens[4]='511192748901567|PO75Ulo6CECzYc9qG-HjSsK6J-U'      
tokens[3]='551320231564366|0st6A6ZIHSTnytvrwPozGoFf260'      
tokens[2]='323755687729999|p-YAUWo1Sc-2hRYPqi9mHUu6_k0'      
tokens[1]='301848573269756|fDJa-7eeto12npt2JpdDO4X7P6E'      
tokens[0]='565607786802000|-zWYLRUaAsvZuJBtZ8NwddhYup0'      
 
 
def get_feeds(id,cs,c_url,to_ins,pg_id,user,processo=1):
 ac=[]
 idk=id
 kuser=user
 errorcks=False
 try:
    args = {}
    
    
    
    args['access_token'] =  tokens[processo-1]
    #args['access_token'],args['limit'] =  tokens[processo-1],'100'

    url='https://graph.facebook.com/'+id+'/feed?' + urllib.urlencode(args)
    #url='https://173.252.73.52/'+id+'/feed?' + urllib.urlencode(args)
    
    
    if c_url != '':
     url=c_url
    
    print 'get page(process):',processo
    file = urllib2.urlopen(url, timeout=5)
    print 'pg.returned...',processo
    
    
    result = simplejson.load(file)    
        
    r2=result['data']
    msg_i=1
    object_id=''
    link=''
    icon=''
    type=''
    message=''
    created_time=''
    story=''
    for ch in r2:     
     try:
      id=ch[u'id']
     except: pass 
     try:
      _from=ch[u'from']
     except: pass 
     try:
      likes=ch[u'likes']
     except: 
      likes=None     
     try:
      message=ch[u'message']
     except: pass 
     try:
      link=ch[u'link']
     except: pass 
     try:
      icon=ch[u'icon']
     except: pass 
     try:
      type=ch[u'type']
     except: pass 
     try:
      status_type=ch[u'status_type']
     except: pass 
     try:
      object_id=ch[u'object_id']
     except: pass 
     try:
      created_time=ch[u'created_time']
     except: pass 
     try:
      updated_time=ch[u'updated_time']
     except: pass 
     try:
      shares=ch[u'shares']
     except: pass 
     try:
      comments=ch[u'comments']
     except: 
      comments=None
      
     try:
      story=ch[u'story']
     except: 
      story=''
       
     if id != None:  
      object_id=id
     from_msg=''
     msg_story=''
     msg_caption=''
     msg_likes='0'
     msg_name=''
     msg_picture=''
     msg_description=''
     from_id=''
     if _from != None:
      msg_name=_from[u'name']
      from_id=_from[u'id']
      
     ac.append( [ from_id,object_id,story,msg_caption,msg_description,msg_picture,link,msg_name,icon,type,msg_likes,message ] )
     
     message=''
     
     if comments != None:
       try:
        its=comments[u'data']
        for it in its:
         created_time=it[u'created_time']
         message=''
         message=it[u'message']
         _from=it[u'from']
         u_name=_from[u'name']
         u_id=_from[u'id']
         #print u_name,u_id
         ac.append( [ u_id,object_id,'','','','',link,u_name,icon,type,'0',message ] )
         #=================
         to_ins.append(['',u_id.encode('latin-1'),u_name.encode('latin-1')])
       except Exception,e: 
          pass       
       
     if likes != None:
       try:
        its=likes[u'data']
        for it in its:
         u_name=it[u'name']
         u_id=it[u'id']
         message='{like}'
         #print u_name,u_id
         ac.append( [ u_id,object_id,'','','','',link,u_name,icon,type,'0',message ] )
         #=================
         to_ins.append(['',u_id.encode('latin-1'),u_name.encode('latin-1')])          
       except Exception,e: 
          pass       
     
     msg_i+=1
       
    post_cmd(to_ins,pg_id,user,idk)
    post_termo(ac,'user','user','igor.moraes','user' )
    closeu(pg_id)
 except Exception,err2:
  print 'Error(2.1):',err2
  log.exception("")
  reopen(pg_id)
  errorcks=True
 

def closeu(ids):
        key=str(ids)
        gt=fcb.get(key)
        gt[u'indexed'] = 'S'
        fcb.insert(key,gt)
        print 'Close usr(1):',ids        


    
def reopen(ids):      
  print 're-open:',ids
  try:
        to_reopen.insert(str(ids),{'ids':str(ids)})
  except: 
   print 'Eror reopen:'
   log.exception("")
      
 
def post_cmd(arr,usr,u_nm,idk):   
  try:
   #print 'insert rows.id(',idk,'):',len(arr)
   for its in arr:
     [a,u_id,u_name]=its
     insere_usr('',u_id,u_name)
     print 'insert-->rows.id:',u_id
  except: 
   log.exception("error insert rowds.id("+str(idk)+")")
  print 'insert',idk,' OK!!'
 
 

def parse(s):
 rt=[]
 tmp=''
 for s1 in s:
  if s1 == ',':
     rt.append(tmp)
     tmp=''
  else:
     tmp+=s1
 return rt      

def entry(params): 
 sents=parse(params) 
 get_feeds(sents[0],0,'',[],int(sents[1]),sents[2],int(sents[3]) )
 
 
 
 
 