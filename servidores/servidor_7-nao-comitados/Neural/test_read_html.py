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

arrno=[]

 


import logging
from StringIO import StringIO
import datetime


logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('read-html')


kl=1

while kl <= 150:
 arrno.append('['+str(kl)+']')
 kl+=1

def cinc(str1c):
 for dd in arrno:
  if dd==str1c: return True
 return False 
 
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.2) Gecko/20090729 Firefox/3.5.2 GTB5')]

def get_page(url):
 global opener
 query=url
 #print 'Open page...' 
 data_Res = opener.open(query, '' ).read()
 #print 'Page open.OK!'
 soup = BeautifulSoup.BeautifulSoup(data_Res)
 h1 = soup.find('h1',id='firstHeading') 
 divc=soup.find('div',id='mw-content-text') 
 title_f=soup.find('h1',id='firstHeading') 
 i=-1
 ln=len(divc.contents)
 #
 strs=[]
 #
 rt=[]
 #
 arr_composi=[]
 arr_table=[]
 print 'Pg.len:',ln 
 while i < ln:
  i+=1
  #print 'Run.ln:',i 
  if i >= ln: break
  elem = divc.contents[i] 
  no_classif_table=False
  if getattr(elem, 'name', None) == 'table':
   try:
    if elem['class']  == 'infobox_v2' :
     for elem2 in elem.contents:     
       if getattr(elem2, 'name', None) == 'tr':
         par=[]
         id_pr=0
         for elem3 in elem2.contents:
          if getattr(elem3, 'name', None) == 'td':
                 
             tx1= elem3.getText(' ').encode('latin-1','ignore')  
              
             tx1=tx1.replace('[1]','')
             tx1=tx1.replace('[2]','')
             tx1=tx1.replace('[3]','')
             tx1=tx1.replace('[4]','')
             tx1=tx1.replace('[5]','')
             tx1=tx1.replace('[6]','')
             tx1=tx1.replace('[6]','')
             tx1=tx1.replace('[8]','')
             tx1=tx1.replace('[9]','')
             tx1=tx1.replace('[10]','')
             tx1=tx1.replace('[11]','')
             tx1=tx1.replace('[12]','')
             tx1=tx1.replace('[13]','')
             tx1=tx1.replace('[14]','')
             tx1=tx1.replace('[15]','')
  
             par.append(tx1+' ')
          if getattr(elem3, 'name', None) == 'th':      
             #print elem3.getText().encode('latin-1', 'ignore')
             par.append(elem3.getText().encode('latin-1', 'ignore'))
             par.append('')
         arr_composi.append(par)
         par=[]       
   except:
     no_classif_table=True
  def process_table(tb):
       #print 'Process.table=================='
       table = tb
       arr_table2=[]
       rows = table.findAll('tr') 
       #cols = rows.findAll('td')
       #===   
       #data = [[td.findChildren(text=True) for td in tr.findAll("td")] for tr in rows]
       data=[]
       posits=[]
       last_len=0   
       tb_f=False
       for tr in rows:         
         tb=tr.findAll("table")
         for t in tb:
           tb_f=True         
         #  
         if tb_f: continue
         #=================
         cs=[]
         indr=0
         for td in tr.findAll("td"): 
           fir_k=False
           col_spec=True
           try:
            att=td['rowspan']
            if not fir_k:
              fir_k=True
              posits=[]
            #
            posits.append([td.findChild(text=True),indr])
           except: 
            col_spec=False
           c=td.findChild(text=True)
           cs.append(c)       
           indr+=1
         if last_len == 0 and len(cs)>0:
           last_len=len(cs)
         elif len(cs) > 0:  
           if len(cs) < last_len :
             for p in posits:
               [dt,idp]=p
               cs.insert(idp,dt)
         if len(cs) > 0 :      
          data.append(cs)  
       titles=[]
       # 
       #print 'process.tb....'
       indr=-1
       all_have_tb=False
       for tr in rows:
         indr+=1
         #print 'process row....',indr
         title1=[]
         #print 'start.row:======================================'
         have_tb=False
         tb=tr.findAll("table")
         for t in tb:
             #print 'process inter.tab=======',indr
             r=process_table(t)
             for r2 in r:
               arr_table2.append(r2)
             have_tb=True
             all_have_tb=True
             #print 'end.inter.tab=============',indr
         if not have_tb and not all_have_tb:         
          for td in tr.findAll("th"):
           t1=td.findChildren(text=True)
           #print '--->',t1
           if len(t1) > 0:
            title1.append(t1[0].encode('latin-1','ignore') )
           else: 
            #print 't1 null --->',t1,'' 
            pass
          if len(title1)>0:
           titles.append(title1)          
       #===============================
       #print 'titles:',titles
       u_titles=[]
       ik=0
       while ik < 50:
        ik+=1
        u_titles.append(None)
       #============================ 
       #print 'read.data:'
       for r in data:
         if len(r)>0:
          arr_table_i=[]
          inda=-1
          for r1 in r:
           if r1 == None or r1 == '\n': continue
           inda+=1
           if len(titles) > 0 :
            arrctmp2=[]   
            ind_title=-1
            for titlesc2 in titles:         
             ind_title+=1 
             if inda < len(titlesc2):
              if r1 != None: r1=r1.encode('latin-1','ignore')
              arrctmp2.append(titlesc2[inda])
              u_titles[ind_title]=titlesc2[inda]
             else: 
              if r1 != None: r1=r1.encode('latin-1','ignore')
              arrctmp2.append(u_titles[ind_title])
            #============
            arr_table_i.append([r1,arrctmp2])
           else:  
             if r1 != None: r1=r1.encode('latin-1','ignore')
             arr_table_i.append([r1,''])
          if len(arr_table_i)>0:   
           arr_table2.append(arr_table_i)  
       return arr_table2       
  if no_classif_table: 
   arr_table=process_table(elem)   
   #print 'arr',arr_table
  if len(arr_table)>0:
    strs.append('\n')
  for tl1 in arr_table:    
      indl=-1
      # procurar se o primeiro ou  o ultimo nao tem somente titulo, para adicionar antes
      for tl in tl1:
       indl+=1
       if tl[0] != None and  tl[0]!=None:
        if umisc.trim(tl[0]) == '' and umisc.trim(tl[1]) != '' :
          strs.append(umisc.trim(tl[1]) + ':\n')
        if umisc.trim(tl[0]) != '' and umisc.trim(tl[1]) == '' :
          strs.append(umisc.trim(tl[0]) + ':\n')
      #
      rt1=''.encode('latin-1')
      for tl in tl1:
       indl+=1
       if tl[0] != None and  tl[0]!=None:
         #rt1+=tl[1] 
         if rt1 != '':
          rt1+=','
         cn=''
         for c1 in tl[1]:
          if cn != '': cn+='>'
          cn+=c1
         rt1+=cn          
         #======         
         rt1+='='
         rt1+=tl[0] 
         #rt1+=',\n'
      strs.append(rt1+';\n')
      
      
  if len(arr_table)> 0 : 
    arr_table=[]
    continue    
  #============================================================ 
  indh=2
  while indh <=10:
   strcmp='h'+str(indh)
   if getattr(elem, 'name', None) == strcmp:
    for elem2 in elem.contents:
      if getattr(elem2, 'name', None) == 'span' :
        if elem2['class']  == 'mw-headline' :
          alc2=elem2.getText().encode('latin-1', 'ignore')
          strs.append(' tema: ' + alc2 + '. ' )
   indh+=1       
  #============================================================     
  if getattr(elem, 'name', None) == 'ul':
   strs.append('\n')
   for elem2 in elem.contents:
     if getattr(elem2, 'name', None) == 'li' :
         alc2=elem2.getText(False).encode('latin-1', 'ignore')
         strs.append(' ' + alc2 + ' ;\n ' )
  #============================================================     
  if getattr(elem, 'name', None) == 'p':
   for d in elem.contents:
    if type(d).__name__ == 'Tag':
     alc= d.getText().encode('latin-1', 'ignore')
     if not cinc(alc):
      strs.append(' ' + alc + ' ' )
    if type(d).__name__ == 'NavigableString':
      tx=d.encode('latin-1', 'ignore')
      if not cinc(tx):
       strs.append(' ' + tx + ' ' )
 #
 txtc2=''.encode('latin-1', 'ignore')
 #
 for a in strs:
   inc1=len(txtc2)-1
   if inc1 >=0:
    if txtc2[inc1]!='': txtc2+=' ' 
   try: 
     cst=a 
     txtc2+=(cst+' '  )
   except: 
     print 'error parse:',a
     log.exception('')
 rt.append(txtc2)  
 #
 #
 agents=''   
 # 
 for ele1 in title_f.contents:
  agents= ele1.getText().encode('latin-1', 'ignore')
  break
 #
 if len(arr_composi) <=0: return []
 agentes=''
 #if agents != '':
 # rt.append(agents) 
 rt.append('\n' )  
 for el in arr_composi  :
  if len(el) >= 2:
   if el[1] == '':
    pass
   else: 
    st= agents + ' característica : ' + el[0] + ' = ' + el[1] + '.' + '\n'
    rt.append(st) 
    
 return rt 
 
  
urlc='http://pt.wikipedia.org/wiki/Miami,_Fl%C3%B3rida'  
#urlc='http://pt.wikipedia.org/wiki/Apple'  
lines=get_page(urlc)
fi= open('txt1','w' )
for ln in lines:
 ln=ln.replace('&#160;','') 
 fi.write(ln)
fi.close()
print 'get.page(OK):' 







  
