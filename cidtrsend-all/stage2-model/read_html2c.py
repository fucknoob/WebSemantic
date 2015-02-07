#coding: latin-1

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
import thread
 
import subprocess
import string

import BeautifulSoup
import umisc 
import bitly

import xml.dom.minidom 


arrno=[]

kl=1

while kl <= 100:
 arrno.append('['+str(kl)+']')
 kl+=1

def cinc(str1c):
 for dd in arrno:
  if dd==str1c: return True
 return False 
 
 
 
def short_url(urllong):
 return bitly.short_url(urllong)
 
def lomadeezar_links(links_tw):
 areturn=[]
 lnk=[]
 ind=1
 for l in links_tw:
   #l=urllib.quote(l)
   lnk.append(['link'+str(ind),l])
   ind+=1
 #url='http://ws.buscape.com/service/createLinks/lomadee/564771466d477a4458664d3d/?sourceId=28009381'+lnk 
 url='http://sandbox.buscape.com/service/createLinks/lomadee/564771466d477a4458664d3d/?' 
 args = {}    
 args['sourceId']='28009381'
 for ul in lnk:
   args[ul[0]]=ul[1]
 dt=urllib.urlencode(args)    
 file = urllib2.urlopen(url,dt)
 data_Resk = file.read()
 #print data_Resk
 dom2 = xml.dom.minidom.parseString(data_Resk)
 nods=dom2.childNodes
 for n1 in nods:
  n2=n1.getElementsByTagName('lomadeeLinks')
  if n2 != None:
   args={}
   for n3 in n2:
    n4=n3.getElementsByTagName('lomadeeLink')
    for n5 in n4:
     for n6 in n5.getElementsByTagName('originalLink'):
      args['originalLink']=n6.firstChild.data
     for n7 in n5.getElementsByTagName('redirectLink'): 
      args['redirectLink']= n7.firstChild.data
     for n8 in n5.getElementsByTagName('code'): 
      args['code']= n8.firstChild.data
     for n9 in n5.getElementsByTagName('id'): 
      args['id']= n9.firstChild.data
     areturn.append(args)
 # 
 # 
 return areturn
 
 
def parse_url_rt(url):
 rt=''
 for u in url:
  if u == '?': break
  rt+=u
 return rt

def parse_metas(soup,orig_url):
 def parse_item(dv):
  t1=dv[0]
  return [t1['name'],t1['content']]
 def parse_q(soup,name):
  divc2=soup.findAll(attrs={"name":name})
  ks= parse_item(divc2)
  return ks
 rt=[] 
 #rt.append( parse_q(soup,"twitter:card") )
 rt.append( parse_q(soup,"twitter:url") )
 #rt.append( parse_q(soup,"twitter:site") )
 #rt.append( parse_q(soup,"twitter:creator") )
 rt.append( parse_q(soup,"twitter:title") )
 rt.append( parse_q(soup,"twitter:description") )
 rt.append( parse_q(soup,"twitter:image") )
 rt.append( [parse_q(soup,"twitter:label1")[1],parse_q(soup,"twitter:data1")[1]] ) 
 rt.append( [parse_q(soup,"twitter:label2")[1],parse_q(soup,"twitter:data2")[1]] ) 
 return rt

 
def parse_page(data_Res,file,orig_url):
 soup = BeautifulSoup.BeautifulSoup(data_Res)
 #
 #metas=parse_metas(soup,orig_url)
 #
 links_to_publish=[]
 #
 lk=lomadeezar_links([orig_url])
 for rturl in lk:
   shorted=short_url(rturl['redirectLink'])
   links_to_publish.append( shorted ) 
 
 print links_to_publish
 
  

 
 
url='http://www.extra.com.br/Moda/RoupasMasculinas/CamisasPolo/Camisa-Polo-Pique-Masculina-The-Great-One-Zebra-Azul-Provence-2472220.html'

query=url

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.2) Gecko/20090729 Firefox/3.5.2 GTB5')]


data_Res = opener.open(query, '' ).read()
file=None
#file = open("c:\\compartilhado\\cmp\\cc.txt", "w")

parse_page(data_Res,file,query)

#file.write(data_Res )

#file.close()


