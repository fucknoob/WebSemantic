#!/usr/bin/env python

#
#	The server that doesn't use the Name Server.
#

import sys, os
import time
 


import pymongo


MONGO_URL='mongodb://mdnet1:acc159753@127.0.0.1:27017/mdnet'
connM = pymongo.Connection(MONGO_URL) 
dbM=connM.mdnet
fcbM=dbM['fcb_users1']

fcbM.update({},{'$set':{'indexed':'N'}},upsert=True,multi=True)





