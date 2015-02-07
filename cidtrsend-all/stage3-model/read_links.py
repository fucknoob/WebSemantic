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

 

 
from BeautifulSoup import BeautifulSoup, SoupStrainer

url='http://www.pontofrio.com.br/'

server=''

query=url

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.2) Gecko/20090729 Firefox/3.5.2 GTB5')]


data_Res = opener.open(query, '' ).read()

collect_u=[]

file = open("c:\\compartilhado\\cmp\\cc2.txt", "w")

for link in BeautifulSoup(data_Res, parseOnlyThese=SoupStrainer('a')):
    if link.has_key('href'):
        if link['href'][0] == '/' and link['href'][1] == '/':
         print 'http:'+link['href'].encode('latin-1')
        else:
         if link['href'][0] != '#':
          collect_u.append(server+link['href'].encode('latin-1'))
          
for c in collect_u:          
 file.write(c+'\n')


 