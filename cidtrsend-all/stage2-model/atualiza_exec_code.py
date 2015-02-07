
def atualiza_code():
    import sys
    sys.path.append('./pymongo')
    sys.path.append('./pycassa')
    import pymongo
    import pycassa
    from pycassa.pool import ConnectionPool
    from pycassa import index
    from pycassa.columnfamily import ColumnFamily 
    #
    pool2 = ConnectionPool('MINDNET', ['79.143.185.3:9160'],timeout=10000000000)
    #
    tb_object1 = pycassa.ColumnFamily(pool2,'SEMANTIC_OBJECT')  
    tb_object_dt1 = pycassa.ColumnFamily(pool2,'SEMANTIC_OBJECT_DT')  
    tb_relaction1 = pycassa.ColumnFamily(pool2,'SEMANTIC_RELACTIONS') 
    tb_know1 = pycassa.ColumnFamily(pool2,'knowledge_manager')
    #
    MONGO_URL='mongodb://mdnet1:acc159753@ds061938.mongolab.com:61938/mdnet' 
    conn = pymongo.Connection(MONGO_URL)
    dbM=conn.mdnet
    #
    tb_object=dbM['SEMANTIC_OBJECT']
    tb_object_dt=dbM['SEMANTIC_OBJECT_DT']
    tb_relaction=dbM['SEMANTIC_RELACTIONS']
    tb_know=dbM['knowledge_manager']
    #
    tb_object.remove()
    tb_object_dt.remove()
    tb_relaction.remove()
    tb_know.remove()
    #
    r1=tb_object1.get_range()
    for k,r  in r1:
      r['id']=k
      tb_object.insert(r)
    #  
    r1=tb_object_dt1.get_range()
    for k,r in r1:
     r['id']=k
     tb_object_dt.insert(r)
     
    r1=tb_relaction1.get_range()
    for k,r in r1:
      r['id']=k
      tb_relaction.insert(r)
    #===   
    r1=tb_know1.get_range()
    for k,r in r1:
       r['id']=k
       tb_know.insert(r)
    #=========================   
 

 


