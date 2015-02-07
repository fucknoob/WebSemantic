import os
import sys
import umisc
 


 
usr='igor.moraes'

import conn
conn2= conn.conn_mx
conn2.sql('delete from web_cache where tps=\'K\'') # tps = K -> importado para analize
conn2.commit()

 

