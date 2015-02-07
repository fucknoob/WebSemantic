
import sys
sys.path.append('/Neural/mxdb')

import maxdb

user = 'MIND'
pwd = 'MIND'
dbname = 'mindnet'
host = '109.235.146.89:3306'

print 'Connecting to host...'

session = maxdb.connect (user, pwd, dbname, host)

print 'Connected...'

'''
stmt = ' insert into kll(c,e,b) values(?,?,?) '
prepar = session.prepare (stmt)
values = [int('90'), int('90') ,'90']
result = prepar.execute (values)

#session.commit()
session.rollback()
'''

try:
 stmt = ' select * from data_behaviour_code where 1=1 or  1>= ?'
 prepar = session.prepare (stmt)
 values = [0]
 result = prepar.execute (values)
except maxdb.sql.SQLError,e: 
 msg=str(e.errorCode)+"["+e.message+"]"
 print( msg )
 sys.exit(0)

row = result.next ()
cc=0
cc1=0
cnt=0
while row:
    #print "\t", row
    cc1+=1
    cnt+=1
    if cc1 > 1000:
     print 'Process:',cnt
     cc1=0
    row = result.next ()
    print row
    #cc+=row[0]

print 'sum:',cc

session.release ()
