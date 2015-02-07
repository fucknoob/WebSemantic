'''tzinfo timezone information for Asia/Tehran.'''
from pytz.tzinfo import DstTzInfo
from pytz.tzinfo import memorized_datetime as d
from pytz.tzinfo import memorized_ttinfo as i

class Tehran(DstTzInfo):
    '''Asia/Tehran timezone definition. See datetime.tzinfo for details'''

    zone = 'Asia/Tehran'

    _utc_transition_times = [
d(1,1,1,0,0,0),
d(1915,12,31,20,34,16),
d(1945,12,31,20,34,16),
d(1977,10,31,20,30,0),
d(1978,3,20,20,0,0),
d(1978,10,20,19,0,0),
d(1978,12,31,20,0,0),
d(1979,3,20,20,30,0),
d(1979,9,18,19,30,0),
d(1980,3,20,20,30,0),
d(1980,9,22,19,30,0),
d(1991,5,2,20,30,0),
d(1991,9,21,19,30,0),
d(1992,3,21,20,30,0),
d(1992,9,21,19,30,0),
d(1993,3,21,20,30,0),
d(1993,9,21,19,30,0),
d(1994,3,21,20,30,0),
d(1994,9,21,19,30,0),
d(1995,3,21,20,30,0),
d(1995,9,21,19,30,0),
d(1996,3,20,20,30,0),
d(1996,9,20,19,30,0),
d(1997,3,21,20,30,0),
d(1997,9,21,19,30,0),
d(1998,3,21,20,30,0),
d(1998,9,21,19,30,0),
d(1999,3,21,20,30,0),
d(1999,9,21,19,30,0),
d(2000,3,20,20,30,0),
d(2000,9,20,19,30,0),
d(2001,3,21,20,30,0),
d(2001,9,21,19,30,0),
d(2002,3,21,20,30,0),
d(2002,9,21,19,30,0),
d(2003,3,21,20,30,0),
d(2003,9,21,19,30,0),
d(2004,3,20,20,30,0),
d(2004,9,20,19,30,0),
d(2005,3,21,20,30,0),
d(2005,9,21,19,30,0),
        ]

    _transition_info = [
i(12360,0,'LMT'),
i(12360,0,'TMT'),
i(12600,0,'IRST'),
i(14400,0,'IRST'),
i(18000,3600,'IRDT'),
i(14400,0,'IRST'),
i(12600,0,'IRST'),
i(16200,3600,'IRDT'),
i(12600,0,'IRST'),
i(16200,3600,'IRDT'),
i(12600,0,'IRST'),
i(16200,3600,'IRDT'),
i(12600,0,'IRST'),
i(16200,3600,'IRDT'),
i(12600,0,'IRST'),
i(16200,3600,'IRDT'),
i(12600,0,'IRST'),
i(16200,3600,'IRDT'),
i(12600,0,'IRST'),
i(16200,3600,'IRDT'),
i(12600,0,'IRST'),
i(16200,3600,'IRDT'),
i(12600,0,'IRST'),
i(16200,3600,'IRDT'),
i(12600,0,'IRST'),
i(16200,3600,'IRDT'),
i(12600,0,'IRST'),
i(16200,3600,'IRDT'),
i(12600,0,'IRST'),
i(16200,3600,'IRDT'),
i(12600,0,'IRST'),
i(16200,3600,'IRDT'),
i(12600,0,'IRST'),
i(16200,3600,'IRDT'),
i(12600,0,'IRST'),
i(16200,3600,'IRDT'),
i(12600,0,'IRST'),
i(16200,3600,'IRDT'),
i(12600,0,'IRST'),
i(16200,3600,'IRDT'),
i(12600,0,'IRST'),
        ]

Tehran = Tehran()

