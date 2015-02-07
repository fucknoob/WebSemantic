import os

import sys
#   
sys.path.append('./dateutil')
sys.path.append('./req')
sys.path.append('./redis')
sys.path.append('./pytz')
sys.path.append('./times')
sys.path.append('./procname')

    
import redis
from rq import Worker, Queue, Connection

listen = ['high', 'default', 'low']

redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')

conn = redis.from_url(redis_url)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()