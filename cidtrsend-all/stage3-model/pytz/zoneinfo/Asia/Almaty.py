'''tzinfo timezone information for Asia/Almaty.'''
from pytz.tzinfo import DstTzInfo
from pytz.tzinfo import memorized_datetime as d
from pytz.tzinfo import memorized_ttinfo as i

class Almaty(DstTzInfo):
    '''Asia/Almaty timezone definition. See datetime.tzinfo for details'''

    zone = 'Asia/Almaty'

    _utc_transition_times = [
d(1,1,1,0,0,0),
d(1924,5,1,18,52,12),
d(1930,6,20,19,0,0),
d(1981,3,31,18,0,0),
d(1981,9,30,17,0,0),
d(1982,3,31,18,0,0),
d(1982,9,30,17,0,0),
d(1983,3,31,18,0,0),
d(1983,9,30,17,0,0),
d(1984,3,31,18,0,0),
d(1984,9,29,20,0,0),
d(1985,3,30,20,0,0),
d(1985,9,28,20,0,0),
d(1986,3,29,20,0,0),
d(1986,9,27,20,0,0),
d(1987,3,28,20,0,0),
d(1987,9,26,20,0,0),
d(1988,3,26,20,0,0),
d(1988,9,24,20,0,0),
d(1989,3,25,20,0,0),
d(1989,9,23,20,0,0),
d(1990,3,24,20,0,0),
d(1990,9,29,20,0,0),
d(1990,12,31,18,0,0),
d(1992,3,28,17,0,0),
d(1992,9,26,16,0,0),
d(1993,3,27,20,0,0),
d(1993,9,25,20,0,0),
d(1994,3,26,20,0,0),
d(1994,9,24,20,0,0),
d(1995,3,25,20,0,0),
d(1995,9,23,20,0,0),
d(1996,3,30,20,0,0),
d(1996,10,26,20,0,0),
d(1997,3,29,20,0,0),
d(1997,10,25,20,0,0),
d(1998,3,28,20,0,0),
d(1998,10,24,20,0,0),
d(1999,3,27,20,0,0),
d(1999,10,30,20,0,0),
d(2000,3,25,20,0,0),
d(2000,10,28,20,0,0),
d(2001,3,24,20,0,0),
d(2001,10,27,20,0,0),
d(2002,3,30,20,0,0),
d(2002,10,26,20,0,0),
d(2003,3,29,20,0,0),
d(2003,10,25,20,0,0),
d(2004,3,27,20,0,0),
d(2004,10,30,20,0,0),
d(2005,3,14,18,0,0),
        ]

    _transition_info = [
i(18480,0,'LMT'),
i(18000,0,'ALMT'),
i(21600,0,'ALMT'),
i(25200,3600,'ALMST'),
i(21600,0,'ALMT'),
i(25200,3600,'ALMST'),
i(21600,0,'ALMT'),
i(25200,3600,'ALMST'),
i(21600,0,'ALMT'),
i(25200,3600,'ALMST'),
i(21600,0,'ALMT'),
i(25200,3600,'ALMST'),
i(21600,0,'ALMT'),
i(25200,3600,'ALMST'),
i(21600,0,'ALMT'),
i(25200,3600,'ALMST'),
i(21600,0,'ALMT'),
i(25200,3600,'ALMST'),
i(21600,0,'ALMT'),
i(25200,3600,'ALMST'),
i(21600,0,'ALMT'),
i(25200,3600,'ALMST'),
i(21600,0,'ALMT'),
i(21600,0,'ALMT'),
i(25200,3600,'ALMST'),
i(21600,0,'ALMT'),
i(25200,3600,'ALMST'),
i(21600,0,'ALMT'),
i(25200,3600,'ALMST'),
i(21600,0,'ALMT'),
i(25200,3600,'ALMST'),
i(21600,0,'ALMT'),
i(25200,3600,'ALMST'),
i(21600,0,'ALMT'),
i(25200,3600,'ALMST'),
i(21600,0,'ALMT'),
i(25200,3600,'ALMST'),
i(21600,0,'ALMT'),
i(25200,3600,'ALMST'),
i(21600,0,'ALMT'),
i(25200,3600,'ALMST'),
i(21600,0,'ALMT'),
i(25200,3600,'ALMST'),
i(21600,0,'ALMT'),
i(25200,3600,'ALMST'),
i(21600,0,'ALMT'),
i(25200,3600,'ALMST'),
i(21600,0,'ALMT'),
i(25200,3600,'ALMST'),
i(21600,0,'ALMT'),
i(21600,0,'ALMT'),
        ]

Almaty = Almaty()

