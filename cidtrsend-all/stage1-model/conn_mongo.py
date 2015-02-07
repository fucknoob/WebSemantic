#conn to mongo
import sys
sys.path.append('./pymongo')
import pymongo


#MONGO_URL='mongodb://mdnet1:acc159753@91.205.172.85:27017/mdnet' 
MONGO_URL='mongodb://mdnet1:acc159753@91.205.172.85:27017/mdnet'
conn = pymongo.Connection(MONGO_URL)
dbM=conn.mdnet

def get_tb():
  web_m=dbM['web_cache']
  return web_m

def get_tb2():
  web_m=dbM['web_cache2']
  return web_m

def get_tb3():
  web_m=dbM['web_cache3']
  return web_m

def get_tb4():
  web_m=dbM['web_cache4']
  return web_m

def get_tb5():
  web_m=dbM['web_cache5']
  return web_m

  