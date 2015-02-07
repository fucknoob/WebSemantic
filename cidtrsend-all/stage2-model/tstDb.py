# tst mysql

import MySQLdb


def entry(req ):
 conn= MySQLdb.connect(host='dbmy0023.whservidor.com', user='mindnet' , passwd='acc159753', db='mindnet')
 cursor = conn.cursor ()
 cursor.execute ("SELECT nome from usuarios")
 row = cursor.fetchone ()
 k=row[0]
 cursor.close ()
 conn.close ()
 return  ("Usuário:"+k )
