
import sys
sys.path.append('./pymongo')
import pymongo


MONGO_URL='mongodb://mdnet1:acc159753@ds061938.mongolab.com:61938/mdnet'
print 'to connect...'
conn = pymongo.Connection(MONGO_URL)
print 'connected.'

 
