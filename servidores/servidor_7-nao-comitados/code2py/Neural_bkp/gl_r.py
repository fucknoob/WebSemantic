#encoding: latin-1

import urllib2
import re
import time
import subprocess
 

def do_reg2(item):
 
    rets=[]
    
    link_re= re.compile('a href=["].*?[\"]')
    links = link_re.findall(item)       
    
    
    for l in links :
        link_re2= re.compile('["].*?[\"]')
        links2 = link_re2.findall(l)       
        #==
        for l2 in links2 :
            lnk = l2.replace('\"', '' )
            if lnk != '#' and lnk[:4] == 'http' :
             text1=item.replace(l2, '')
             text2=text1.replace('</a>', '')
             text2=text1.replace(' \'\">','')
             text2=text2.replace('<a href= >','')
             text2=text2.replace('\">','')
             text2=text2.replace('</a>','')
             text2=text2.replace('<em>','')
             text2=text2.replace('</em>','')
             text2=text2.replace('<b>.','')
             text2=text2.replace('</b>','')
             rets.append([lnk,text2]) 

 
    return  rets;
 

def do_reg( text2):
        
    
    text=text2;
    rets2=[]
    # 
    link_re= re.compile('class=l onmousedown=[\"].*?[\"]')
    links = link_re.findall(text2)    
    if links:
     for l in links:
      text=text.replace(l,'') 
 
      
    text2=text   

 
    
    link_re = re.compile("<h3 class=\"r(.*?)</h3>")
    links2 = link_re.findall(text2)        
    if links2:     
     for l2 in links2:
        it2= l2.replace('<h3 class=\"r\">', '' )
        it3= it2.replace('</h3>', '')
 
        r=do_reg2(it3);
        for d in r:
         rets2.append(d)
 
    return rets2
    

def open_pg(endereco):    
 proc = subprocess.Popen("php /home/mdnetsocia/public_html/get_Text.php q="+endereco, shell=True,stdout=subprocess.PIPE)
 script_response = proc.stdout.read()
 return script_response    
    
def run(qr,icount):
 
 reps= int(icount/100)
 if reps < 1 : reps=1
 rel=[]
 r1=0
 while r1 < reps:
  istart=(r1*100)+1
  print 'Search....:',istart,'[',r1,',',reps,']'
  url='http://www.google.com/search?hl=pt&num='+str(icount)+'&start='+str(istart)+'&safe=off&q='+qr
  opener = urllib2.build_opener ()
  opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.2) Gecko/20090729 Firefox/3.5.2 GTB5')]
  response = opener.open(url).read () 
   
 
  s=do_reg(response)
  cnts=len(s)
  id=0
  for a in s :
   id+=1
   print 'Ln:',id,' of:',cnts   
   #===========================================
   # a[0]=endereco,a[1]=titulo
   #===========================================
   aa=[a[0],a[1],open_pg(a[0]) ]
   rel.append(aa)
   #rel.append(a)
  
  r1+=1
  
 return rel
 
''' 
c= run('carro',10) 
f=open('/home/mdnetsocia/kk.txt','w');
for c1 in c:
 for c2 in c1:
  f.write(c2);
 f.write('\n')
f.close()
''' 
 

 

