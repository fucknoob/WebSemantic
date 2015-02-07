'''tzinfo timezone information for Europe/Kaliningrad.'''
from pytz.tzinfo import DstTzInfo
from pytz.tzinfo import memorized_datetime as d
from pytz.tzinfo import memorized_ttinfo as i

class Kaliningrad(DstTzInfo):
    '''Europe/Kaliningrad timezone definition. See datetime.tzinfo for details'''

    zone = 'Europe/Kaliningrad'

    _utc_transition_times = [
d(1,1,1,0,0,0),
d(1916,4,30,22,0,0),
d(1916,9,30,23,0,0),
d(1917,4,16,1,0,0),
d(1917,9,17,1,0,0),
d(1918,4,15,1,0,0),
d(1918,9,16,1,0,0),
d(1940,4,1,1,0,0),
d(1942,11,2,1,0,0),
d(1943,3,29,1,0,0),
d(1943,10,4,1,0,0),
d(1944,4,3,1,0,0),
d(1944,10,2,1,0,0),
d(1944,12,31,23,0,0),
d(1945,4,28,22,0,0),
d(1945,10,31,21,0,0),
d(1945,12,31,22,0,0),
d(1981,3,31,21,0,0),
d(1981,9,30,20,0,0),
d(1982,3,31,21,0,0),
d(1982,9,30,20,0,0),
d(1983,3,31,21,0,0),
d(1983,9,30,20,0,0),
d(1984,3,31,21,0,0),
d(1984,9,29,23,0,0),
d(1985,3,30,23,0,0),
d(1985,9,28,23,0,0),
d(1986,3,29,23,0,0),
d(1986,9,27,23,0,0),
d(1987,3,28,23,0,0),
d(1987,9,26,23,0,0),
d(1988,3,26,23,0,0),
d(1988,9,24,23,0,0),
d(1989,3,25,23,0,0),
d(1989,9,23,23,0,0),
d(1990,3,24,23,0,0),
d(1990,9,29,23,0,0),
d(1991,3,30,23,0,0),
d(1991,9,29,0,0,0),
d(1992,3,28,21,0,0),
d(1992,9,26,20,0,0),
d(1993,3,28,0,0,0),
d(1993,9,26,0,0,0),
d(1994,3,27,0,0,0),
d(1994,9,25,0,0,0),
d(1995,3,26,0,0,0),
d(1995,9,24,0,0,0),
d(1996,3,31,0,0,0),
d(1996,10,27,0,0,0),
d(1997,3,30,0,0,0),
d(1997,10,26,0,0,0),
d(1998,3,29,0,0,0),
d(1998,10,25,0,0,0),
d(1999,3,28,0,0,0),
d(1999,10,31,0,0,0),
d(2000,3,26,0,0,0),
d(2000,10,29,0,0,0),
d(2001,3,25,0,0,0),
d(2001,10,28,0,0,0),
d(2002,3,31,0,0,0),
d(2002,10,27,0,0,0),
d(2003,3,30,0,0,0),
d(2003,10,26,0,0,0),
d(2004,3,28,0,0,0),
d(2004,10,31,0,0,0),
d(2005,3,27,0,0,0),
d(2005,10,30,0,0,0),
d(2006,3,26,0,0,0),
d(2006,10,29,0,0,0),
d(2007,3,25,0,0,0),
d(2007,10,28,0,0,0),
d(2008,3,30,0,0,0),
d(2008,10,26,0,0,0),
d(2009,3,29,0,0,0),
d(2009,10,25,0,0,0),
d(2010,3,28,0,0,0),
d(2010,10,31,0,0,0),
d(2011,3,27,0,0,0),
d(2011,10,30,0,0,0),
d(2012,3,25,0,0,0),
d(2012,10,28,0,0,0),
d(2013,3,31,0,0,0),
d(2013,10,27,0,0,0),
d(2014,3,30,0,0,0),
d(2014,10,26,0,0,0),
d(2015,3,29,0,0,0),
d(2015,10,25,0,0,0),
d(2016,3,27,0,0,0),
d(2016,10,30,0,0,0),
d(2017,3,26,0,0,0),
d(2017,10,29,0,0,0),
d(2018,3,25,0,0,0),
d(2018,10,28,0,0,0),
d(2019,3,31,0,0,0),
d(2019,10,27,0,0,0),
d(2020,3,29,0,0,0),
d(2020,10,25,0,0,0),
d(2021,3,28,0,0,0),
d(2021,10,31,0,0,0),
d(2022,3,27,0,0,0),
d(2022,10,30,0,0,0),
d(2023,3,26,0,0,0),
d(2023,10,29,0,0,0),
d(2024,3,31,0,0,0),
d(2024,10,27,0,0,0),
d(2025,3,30,0,0,0),
d(2025,10,26,0,0,0),
d(2026,3,29,0,0,0),
d(2026,10,25,0,0,0),
d(2027,3,28,0,0,0),
d(2027,10,31,0,0,0),
d(2028,3,26,0,0,0),
d(2028,10,29,0,0,0),
d(2029,3,25,0,0,0),
d(2029,10,28,0,0,0),
d(2030,3,31,0,0,0),
d(2030,10,27,0,0,0),
d(2031,3,30,0,0,0),
d(2031,10,26,0,0,0),
d(2032,3,28,0,0,0),
d(2032,10,31,0,0,0),
d(2033,3,27,0,0,0),
d(2033,10,30,0,0,0),
d(2034,3,26,0,0,0),
d(2034,10,29,0,0,0),
d(2035,3,25,0,0,0),
d(2035,10,28,0,0,0),
d(2036,3,30,0,0,0),
d(2036,10,26,0,0,0),
d(2037,3,29,0,0,0),
d(2037,10,25,0,0,0),
        ]

    _transition_info = [
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,0,'CET'),
i(10800,3600,'CEST'),
i(7200,0,'CET'),
i(10800,0,'MSK'),
i(14400,3600,'MSD'),
i(10800,0,'MSK'),
i(14400,3600,'MSD'),
i(10800,0,'MSK'),
i(14400,3600,'MSD'),
i(10800,0,'MSK'),
i(14400,3600,'MSD'),
i(10800,0,'MSK'),
i(14400,3600,'MSD'),
i(10800,0,'MSK'),
i(14400,3600,'MSD'),
i(10800,0,'MSK'),
i(14400,3600,'MSD'),
i(10800,0,'MSK'),
i(14400,3600,'MSD'),
i(10800,0,'MSK'),
i(14400,3600,'MSD'),
i(10800,0,'MSK'),
i(14400,3600,'MSD'),
i(10800,0,'MSK'),
i(10800,0,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
        ]

Kaliningrad = Kaliningrad()

