from mod_python import apache

import base64
import calendar
import os
import rfc822
import sys
import tempfile
import textwrap
import time
import urllib
import urllib2
import urlparse
import cookielib

import sys
#sys.path.append('/var/www/html/PY')
#sys.path.append('/var/www/html/PY/simplejson')

import simplejson 
 
 
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('Referer', 'http://login.facebook.com/login.php'),('Content-Type', 'application/x-www-form-urlencoded'),('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7 (.NET CLR 3.5.30729)')]


 
def facebook_search(query,uuid):
    r=[]
    ids=['4','454972255187','154208488015206','433953520005784','155969044473475','1712901870','100001806368318','1719355104','100002147765250','1310103835'] 
    for _id in ids:
     #
     #texto_resultado='<iframe src=\\\'http://www.terra.com.br\\\'></iframe>'; 
     texto_resultado='asssssssssssssssssssssssssssss<br>bbbbbbbbbbbbbbbb<br>ccccccccccccccc<br>uuid:'+uuid;
     url2='http://graph.facebook.com/'+_id
     result2 = simplejson.load(urllib.urlopen(url2))
     name=''
     resume='resumo do texto'
     resume2='resumo do texto2'
     try:
      name=result2['name']
     except:
      name=''     
     user=''
     try:
      user=result2['username']
     except:
        user=''     
     #first_name
     #middle_name
     #last_name
     #"gender": "male",
     #"locale": "pt_BR"
     #link     
     #=======================================================
     if name != ''  and user != '' :
      url_picture_less='http://graph.facebook.com/'+_id+'/picture'
      url_picture_large='http://graph.facebook.com/'+_id+'/picture?width=140&height=140'
      msg_picture=None
      usock = opener.open(url_picture_less)
      finalurl = usock.geturl()  
      r.append({"name":name,"user":user,"finalurl":finalurl,"texto_resultado":texto_resultado,"resume":resume,"resume2":resume2})
    #========== 
    return r     


import simplejson as json
''' 
def entry(req,query,callback):
 query=urllib.quote(query)
 rt= facebook_search(query)
 rs=json.dumps(rt)
 r1=callback+"("+rs+");" 
 #=======================================
 #====
 return rs
'''
 
def entry(req,query,callback,uuid):
 query=urllib.quote(query)
 rt= facebook_search(query,uuid)
 rs=json.dumps(rt)
 r1=callback+"({\"rows\":"+rs+",\"total\":\"10\"});" 
 #=======================================
 #====
 return r1
 
 
 