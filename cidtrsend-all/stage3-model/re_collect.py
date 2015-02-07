#coding: latin-1
# insere usuarios avulsos


import os
import sys

sys.path.append('./pymongo')  
import pymongo


MONGO_URL='mongodb://mdnet1:acc159753@ds061938.mongolab.com:61938/mdnet'
connM = pymongo.Connection(MONGO_URL) 
dbM=connM.mdnet1
fcb=dbM['fcb_users']

web=dbM['web_cache']

r=fcb.find({})
for c in r:
 c['indexed']='N'
 fcb.update({'_id':c['_id']},c)
 
#update({'_id':213}, {'$set':{"jobs.1.title":1}}, upsert=False, multi=True) 
web.update({},{"$set": {'processed':'N'}},upsert=False,multi=True) 
 
 

 