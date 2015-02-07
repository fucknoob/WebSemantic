#coding: latin-1
#
#
#coletar urls do extra --> twitter:url sao as paginas finais
# cache_products -> tabela com os links diretos pros produtos, sem paginas intermediarias de links


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
import umisc 
import bitly
import time

import xml.dom.minidom 

import pycassa
from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily
from pycassa import index


#pool2 = ConnectionPool('MINDNET', ['79.143.185.3:9160'],timeout=10)

pool2 = ConnectionPool('MINDNET', ['79.143.185.3:9160'],timeout=10)

tab2 = pycassa.ColumnFamily(pool2, 'cache_products')
tab3 = pycassa.ColumnFamily(pool2, 'cache_links') # links temporarios



tb_object_dt = pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT_DT3') 
tb_object = pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT3') 
tb_object_relaction = pycassa.ColumnFamily(pool2, 'SEMANTIC_RELACTIONS3') 


tb_object_dt3 = pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT_DT3_1_4') 
tb_object3 = pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT3_1_4') 
tb_object_relaction3 = pycassa.ColumnFamily(pool2, 'SEMANTIC_RELACTIONS3_1_4') 


tb_object.truncate()
tb_object3.truncate()

tb_object_dt.truncate()
tb_object_dt3.truncate()

tb_object_relaction.truncate()
tb_object_relaction3.truncate()


tab2.truncate()
tab3.truncate()


tab4 = pycassa.ColumnFamily(pool2, 'web_cache1')
tab5 = pycassa.ColumnFamily(pool2, 'fcb_users1')


tab4.truncate()
tab5.truncate()
