'''tzinfo timezone information for Europe/Madrid.'''
from pytz.tzinfo import DstTzInfo
from pytz.tzinfo import memorized_datetime as d
from pytz.tzinfo import memorized_ttinfo as i

class Madrid(DstTzInfo):
    '''Europe/Madrid timezone definition. See datetime.tzinfo for details'''

    zone = 'Europe/Madrid'

    _utc_transition_times = [
d(1,1,1,0,0,0),
d(1917,5,5,23,0,0),
d(1917,10,6,23,0,0),
d(1918,4,15,23,0,0),
d(1918,10,6,23,0,0),
d(1919,4,5,23,0,0),
d(1919,10,6,23,0,0),
d(1924,4,16,23,0,0),
d(1924,10,4,23,0,0),
d(1926,4,17,23,0,0),
d(1926,10,2,23,0,0),
d(1927,4,9,23,0,0),
d(1927,10,1,23,0,0),
d(1928,4,14,23,0,0),
d(1928,10,6,23,0,0),
d(1929,4,20,23,0,0),
d(1929,10,5,23,0,0),
d(1937,5,22,23,0,0),
d(1937,10,2,23,0,0),
d(1938,3,22,23,0,0),
d(1938,10,1,23,0,0),
d(1939,4,15,23,0,0),
d(1939,10,7,23,0,0),
d(1940,3,16,23,0,0),
d(1942,5,2,22,0,0),
d(1942,9,1,22,0,0),
d(1943,4,17,22,0,0),
d(1943,10,3,22,0,0),
d(1944,4,15,22,0,0),
d(1944,10,10,22,0,0),
d(1945,4,14,22,0,0),
d(1945,9,29,23,0,0),
d(1946,4,13,22,0,0),
d(1946,9,29,22,0,0),
d(1949,4,30,22,0,0),
d(1949,9,29,23,0,0),
d(1974,4,13,22,0,0),
d(1974,10,5,23,0,0),
d(1975,4,19,22,0,0),
d(1975,10,4,23,0,0),
d(1976,3,27,22,0,0),
d(1976,9,25,23,0,0),
d(1977,4,2,22,0,0),
d(1977,9,24,23,0,0),
d(1978,4,2,22,0,0),
d(1978,9,30,23,0,0),
d(1979,4,1,1,0,0),
d(1979,9,30,1,0,0),
d(1980,4,6,1,0,0),
d(1980,9,28,1,0,0),
d(1981,3,29,1,0,0),
d(1981,9,27,1,0,0),
d(1982,3,28,1,0,0),
d(1982,9,26,1,0,0),
d(1983,3,27,1,0,0),
d(1983,9,25,1,0,0),
d(1984,3,25,1,0,0),
d(1984,9,30,1,0,0),
d(1985,3,31,1,0,0),
d(1985,9,29,1,0,0),
d(1986,3,30,1,0,0),
d(1986,9,28,1,0,0),
d(1987,3,29,1,0,0),
d(1987,9,27,1,0,0),
d(1988,3,27,1,0,0),
d(1988,9,25,1,0,0),
d(1989,3,26,1,0,0),
d(1989,9,24,1,0,0),
d(1990,3,25,1,0,0),
d(1990,9,30,1,0,0),
d(1991,3,31,1,0,0),
d(1991,9,29,1,0,0),
d(1992,3,29,1,0,0),
d(1992,9,27,1,0,0),
d(1993,3,28,1,0,0),
d(1993,9,26,1,0,0),
d(1994,3,27,1,0,0),
d(1994,9,25,1,0,0),
d(1995,3,26,1,0,0),
d(1995,9,24,1,0,0),
d(1996,3,31,1,0,0),
d(1996,10,27,1,0,0),
d(1997,3,30,1,0,0),
d(1997,10,26,1,0,0),
d(1998,3,29,1,0,0),
d(1998,10,25,1,0,0),
d(1999,3,28,1,0,0),
d(1999,10,31,1,0,0),
d(2000,3,26,1,0,0),
d(2000,10,29,1,0,0),
d(2001,3,25,1,0,0),
d(2001,10,28,1,0,0),
d(2002,3,31,1,0,0),
d(2002,10,27,1,0,0),
d(2003,3,30,1,0,0),
d(2003,10,26,1,0,0),
d(2004,3,28,1,0,0),
d(2004,10,31,1,0,0),
d(2005,3,27,1,0,0),
d(2005,10,30,1,0,0),
d(2006,3,26,1,0,0),
d(2006,10,29,1,0,0),
d(2007,3,25,1,0,0),
d(2007,10,28,1,0,0),
d(2008,3,30,1,0,0),
d(2008,10,26,1,0,0),
d(2009,3,29,1,0,0),
d(2009,10,25,1,0,0),
d(2010,3,28,1,0,0),
d(2010,10,31,1,0,0),
d(2011,3,27,1,0,0),
d(2011,10,30,1,0,0),
d(2012,3,25,1,0,0),
d(2012,10,28,1,0,0),
d(2013,3,31,1,0,0),
d(2013,10,27,1,0,0),
d(2014,3,30,1,0,0),
d(2014,10,26,1,0,0),
d(2015,3,29,1,0,0),
d(2015,10,25,1,0,0),
d(2016,3,27,1,0,0),
d(2016,10,30,1,0,0),
d(2017,3,26,1,0,0),
d(2017,10,29,1,0,0),
d(2018,3,25,1,0,0),
d(2018,10,28,1,0,0),
d(2019,3,31,1,0,0),
d(2019,10,27,1,0,0),
d(2020,3,29,1,0,0),
d(2020,10,25,1,0,0),
d(2021,3,28,1,0,0),
d(2021,10,31,1,0,0),
d(2022,3,27,1,0,0),
d(2022,10,30,1,0,0),
d(2023,3,26,1,0,0),
d(2023,10,29,1,0,0),
d(2024,3,31,1,0,0),
d(2024,10,27,1,0,0),
d(2025,3,30,1,0,0),
d(2025,10,26,1,0,0),
d(2026,3,29,1,0,0),
d(2026,10,25,1,0,0),
d(2027,3,28,1,0,0),
d(2027,10,31,1,0,0),
d(2028,3,26,1,0,0),
d(2028,10,29,1,0,0),
d(2029,3,25,1,0,0),
d(2029,10,28,1,0,0),
d(2030,3,31,1,0,0),
d(2030,10,27,1,0,0),
d(2031,3,30,1,0,0),
d(2031,10,26,1,0,0),
d(2032,3,28,1,0,0),
d(2032,10,31,1,0,0),
d(2033,3,27,1,0,0),
d(2033,10,30,1,0,0),
d(2034,3,26,1,0,0),
d(2034,10,29,1,0,0),
d(2035,3,25,1,0,0),
d(2035,10,28,1,0,0),
d(2036,3,30,1,0,0),
d(2036,10,26,1,0,0),
d(2037,3,29,1,0,0),
d(2037,10,25,1,0,0),
        ]

    _transition_info = [
i(0,0,'WET'),
i(3600,3600,'WEST'),
i(0,0,'WET'),
i(3600,3600,'WEST'),
i(0,0,'WET'),
i(3600,3600,'WEST'),
i(0,0,'WET'),
i(3600,3600,'WEST'),
i(0,0,'WET'),
i(3600,3600,'WEST'),
i(0,0,'WET'),
i(3600,3600,'WEST'),
i(0,0,'WET'),
i(3600,3600,'WEST'),
i(0,0,'WET'),
i(3600,3600,'WEST'),
i(0,0,'WET'),
i(3600,3600,'WEST'),
i(0,0,'WET'),
i(3600,3600,'WEST'),
i(0,0,'WET'),
i(3600,3600,'WEST'),
i(0,0,'WET'),
i(3600,3600,'WEST'),
i(7200,7200,'WEMT'),
i(3600,3600,'WEST'),
i(7200,7200,'WEMT'),
i(3600,3600,'WEST'),
i(7200,7200,'WEMT'),
i(3600,3600,'WEST'),
i(7200,7200,'WEMT'),
i(3600,3600,'WEST'),
i(7200,7200,'WEMT'),
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
        ]

Madrid = Madrid()

