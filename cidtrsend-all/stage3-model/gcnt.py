import sys
import os


import bson

import pymongo

#file:200

print 'Connect to mongo...'
MONGO_URL='mongodb://mdnet1:acc159753@127.0.0.1:27017/mdnet'
connM = pymongo.Connection(MONGO_URL) 
dbM=connM.mdnet
fcbM=dbM['fcb_users']
 
print 'total :',fcbM.count()
      
  