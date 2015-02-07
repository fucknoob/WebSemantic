#coding: latin-1
# insere usuarios avulsos


import os
import sys

sys.path.append('./pymongo')  
import pymongo


MONGO_URL='mongodb://mdnet1:acc159753@ds061938.mongolab.com:61938/mdnet'
connM = pymongo.Connection(MONGO_URL) 
dbM=connM.mdnet
web=dbM['web_cache']

r=web.find({"processed":"S"}).count()
print r
 
