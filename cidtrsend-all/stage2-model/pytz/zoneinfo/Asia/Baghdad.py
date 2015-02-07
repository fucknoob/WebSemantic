'''tzinfo timezone information for Asia/Baghdad.'''
from pytz.tzinfo import DstTzInfo
from pytz.tzinfo import memorized_datetime as d
from pytz.tzinfo import memorized_ttinfo as i

class Baghdad(DstTzInfo):
    '''Asia/Baghdad timezone definition. See datetime.tzinfo for details'''

    zone = 'Asia/Baghdad'

    _utc_transition_times = [
d(1,1,1,0,0,0),
d(1917,12,31,21,2,24),
d(1982,4,30,21,0,0),
d(1982,9,30,20,0,0),
d(1983,3,30,21,0,0),
d(1983,9,30,20,0,0),
d(1984,3,31,21,0,0),
d(1984,9,30,20,0,0),
d(1985,3,31,21,0,0),
d(1985,9,28,22,0,0),
d(1986,3,29,22,0,0),
d(1986,9,27,22,0,0),
d(1987,3,28,22,0,0),
d(1987,9,26,22,0,0),
d(1988,3,26,22,0,0),
d(1988,9,24,22,0,0),
d(1989,3,25,22,0,0),
d(1989,9,23,22,0,0),
d(1990,3,24,22,0,0),
d(1990,9,29,22,0,0),
d(1991,4,1,0,0,0),
d(1991,10,1,0,0,0),
d(1992,4,1,0,0,0),
d(1992,10,1,0,0,0),
d(1993,4,1,0,0,0),
d(1993,10,1,0,0,0),
d(1994,4,1,0,0,0),
d(1994,10,1,0,0,0),
d(1995,4,1,0,0,0),
d(1995,10,1,0,0,0),
d(1996,4,1,0,0,0),
d(1996,10,1,0,0,0),
d(1997,4,1,0,0,0),
d(1997,10,1,0,0,0),
d(1998,4,1,0,0,0),
d(1998,10,1,0,0,0),
d(1999,4,1,0,0,0),
d(1999,10,1,0,0,0),
d(2000,4,1,0,0,0),
d(2000,10,1,0,0,0),
d(2001,4,1,0,0,0),
d(2001,10,1,0,0,0),
d(2002,4,1,0,0,0),
d(2002,10,1,0,0,0),
d(2003,4,1,0,0,0),
d(2003,10,1,0,0,0),
d(2004,4,1,0,0,0),
d(2004,10,1,0,0,0),
d(2005,4,1,0,0,0),
d(2005,10,1,0,0,0),
d(2006,4,1,0,0,0),
d(2006,10,1,0,0,0),
d(2007,4,1,0,0,0),
d(2007,10,1,0,0,0),
d(2008,4,1,0,0,0),
d(2008,10,1,0,0,0),
d(2009,4,1,0,0,0),
d(2009,10,1,0,0,0),
d(2010,4,1,0,0,0),
d(2010,10,1,0,0,0),
d(2011,4,1,0,0,0),
d(2011,10,1,0,0,0),
d(2012,4,1,0,0,0),
d(2012,10,1,0,0,0),
d(2013,4,1,0,0,0),
d(2013,10,1,0,0,0),
d(2014,4,1,0,0,0),
d(2014,10,1,0,0,0),
d(2015,4,1,0,0,0),
d(2015,10,1,0,0,0),
d(2016,4,1,0,0,0),
d(2016,10,1,0,0,0),
d(2017,4,1,0,0,0),
d(2017,10,1,0,0,0),
d(2018,4,1,0,0,0),
d(2018,10,1,0,0,0),
d(2019,4,1,0,0,0),
d(2019,10,1,0,0,0),
d(2020,4,1,0,0,0),
d(2020,10,1,0,0,0),
d(2021,4,1,0,0,0),
d(2021,10,1,0,0,0),
d(2022,4,1,0,0,0),
d(2022,10,1,0,0,0),
d(2023,4,1,0,0,0),
d(2023,10,1,0,0,0),
d(2024,4,1,0,0,0),
d(2024,10,1,0,0,0),
d(2025,4,1,0,0,0),
d(2025,10,1,0,0,0),
d(2026,4,1,0,0,0),
d(2026,10,1,0,0,0),
d(2027,4,1,0,0,0),
d(2027,10,1,0,0,0),
d(2028,4,1,0,0,0),
d(2028,10,1,0,0,0),
d(2029,4,1,0,0,0),
d(2029,10,1,0,0,0),
d(2030,4,1,0,0,0),
d(2030,10,1,0,0,0),
d(2031,4,1,0,0,0),
d(2031,10,1,0,0,0),
d(2032,4,1,0,0,0),
d(2032,10,1,0,0,0),
d(2033,4,1,0,0,0),
d(2033,10,1,0,0,0),
d(2034,4,1,0,0,0),
d(2034,10,1,0,0,0),
d(2035,4,1,0,0,0),
d(2035,10,1,0,0,0),
d(2036,4,1,0,0,0),
d(2036,10,1,0,0,0),
d(2037,4,1,0,0,0),
d(2037,10,1,0,0,0),
        ]

    _transition_info = [
i(10680,0,'BMT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
i(14400,3600,'ADT'),
i(10800,0,'AST'),
        ]

Baghdad = Baghdad()

