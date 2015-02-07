'''tzinfo timezone information for US/Eastern.'''
from pytz.tzinfo import DstTzInfo
from pytz.tzinfo import memorized_datetime as d
from pytz.tzinfo import memorized_ttinfo as i

class Eastern(DstTzInfo):
    '''US/Eastern timezone definition. See datetime.tzinfo for details'''

    zone = 'US/Eastern'

    _utc_transition_times = [
d(1,1,1,0,0,0),
d(1918,3,31,7,0,0),
d(1918,10,27,6,0,0),
d(1919,3,30,7,0,0),
d(1919,10,26,6,0,0),
d(1920,3,28,7,0,0),
d(1920,10,31,6,0,0),
d(1921,4,24,7,0,0),
d(1921,9,25,6,0,0),
d(1922,4,30,7,0,0),
d(1922,9,24,6,0,0),
d(1923,4,29,7,0,0),
d(1923,9,30,6,0,0),
d(1924,4,27,7,0,0),
d(1924,9,28,6,0,0),
d(1925,4,26,7,0,0),
d(1925,9,27,6,0,0),
d(1926,4,25,7,0,0),
d(1926,9,26,6,0,0),
d(1927,4,24,7,0,0),
d(1927,9,25,6,0,0),
d(1928,4,29,7,0,0),
d(1928,9,30,6,0,0),
d(1929,4,28,7,0,0),
d(1929,9,29,6,0,0),
d(1930,4,27,7,0,0),
d(1930,9,28,6,0,0),
d(1931,4,26,7,0,0),
d(1931,9,27,6,0,0),
d(1932,4,24,7,0,0),
d(1932,9,25,6,0,0),
d(1933,4,30,7,0,0),
d(1933,9,24,6,0,0),
d(1934,4,29,7,0,0),
d(1934,9,30,6,0,0),
d(1935,4,28,7,0,0),
d(1935,9,29,6,0,0),
d(1936,4,26,7,0,0),
d(1936,9,27,6,0,0),
d(1937,4,25,7,0,0),
d(1937,9,26,6,0,0),
d(1938,4,24,7,0,0),
d(1938,9,25,6,0,0),
d(1939,4,30,7,0,0),
d(1939,9,24,6,0,0),
d(1940,4,28,7,0,0),
d(1940,9,29,6,0,0),
d(1941,4,27,7,0,0),
d(1941,9,28,6,0,0),
d(1942,2,9,7,0,0),
d(1945,8,14,23,0,0),
d(1945,9,30,6,0,0),
d(1946,4,28,7,0,0),
d(1946,9,29,6,0,0),
d(1947,4,27,7,0,0),
d(1947,9,28,6,0,0),
d(1948,4,25,7,0,0),
d(1948,9,26,6,0,0),
d(1949,4,24,7,0,0),
d(1949,9,25,6,0,0),
d(1950,4,30,7,0,0),
d(1950,9,24,6,0,0),
d(1951,4,29,7,0,0),
d(1951,9,30,6,0,0),
d(1952,4,27,7,0,0),
d(1952,9,28,6,0,0),
d(1953,4,26,7,0,0),
d(1953,9,27,6,0,0),
d(1954,4,25,7,0,0),
d(1954,9,26,6,0,0),
d(1955,4,24,7,0,0),
d(1955,10,30,6,0,0),
d(1956,4,29,7,0,0),
d(1956,10,28,6,0,0),
d(1957,4,28,7,0,0),
d(1957,10,27,6,0,0),
d(1958,4,27,7,0,0),
d(1958,10,26,6,0,0),
d(1959,4,26,7,0,0),
d(1959,10,25,6,0,0),
d(1960,4,24,7,0,0),
d(1960,10,30,6,0,0),
d(1961,4,30,7,0,0),
d(1961,10,29,6,0,0),
d(1962,4,29,7,0,0),
d(1962,10,28,6,0,0),
d(1963,4,28,7,0,0),
d(1963,10,27,6,0,0),
d(1964,4,26,7,0,0),
d(1964,10,25,6,0,0),
d(1965,4,25,7,0,0),
d(1965,10,31,6,0,0),
d(1966,4,24,7,0,0),
d(1966,10,30,6,0,0),
d(1967,4,30,7,0,0),
d(1967,10,29,6,0,0),
d(1968,4,28,7,0,0),
d(1968,10,27,6,0,0),
d(1969,4,27,7,0,0),
d(1969,10,26,6,0,0),
d(1970,4,26,7,0,0),
d(1970,10,25,6,0,0),
d(1971,4,25,7,0,0),
d(1971,10,31,6,0,0),
d(1972,4,30,7,0,0),
d(1972,10,29,6,0,0),
d(1973,4,29,7,0,0),
d(1973,10,28,6,0,0),
d(1974,1,6,7,0,0),
d(1974,10,27,6,0,0),
d(1975,2,23,7,0,0),
d(1975,10,26,6,0,0),
d(1976,4,25,7,0,0),
d(1976,10,31,6,0,0),
d(1977,4,24,7,0,0),
d(1977,10,30,6,0,0),
d(1978,4,30,7,0,0),
d(1978,10,29,6,0,0),
d(1979,4,29,7,0,0),
d(1979,10,28,6,0,0),
d(1980,4,27,7,0,0),
d(1980,10,26,6,0,0),
d(1981,4,26,7,0,0),
d(1981,10,25,6,0,0),
d(1982,4,25,7,0,0),
d(1982,10,31,6,0,0),
d(1983,4,24,7,0,0),
d(1983,10,30,6,0,0),
d(1984,4,29,7,0,0),
d(1984,10,28,6,0,0),
d(1985,4,28,7,0,0),
d(1985,10,27,6,0,0),
d(1986,4,27,7,0,0),
d(1986,10,26,6,0,0),
d(1987,4,5,7,0,0),
d(1987,10,25,6,0,0),
d(1988,4,3,7,0,0),
d(1988,10,30,6,0,0),
d(1989,4,2,7,0,0),
d(1989,10,29,6,0,0),
d(1990,4,1,7,0,0),
d(1990,10,28,6,0,0),
d(1991,4,7,7,0,0),
d(1991,10,27,6,0,0),
d(1992,4,5,7,0,0),
d(1992,10,25,6,0,0),
d(1993,4,4,7,0,0),
d(1993,10,31,6,0,0),
d(1994,4,3,7,0,0),
d(1994,10,30,6,0,0),
d(1995,4,2,7,0,0),
d(1995,10,29,6,0,0),
d(1996,4,7,7,0,0),
d(1996,10,27,6,0,0),
d(1997,4,6,7,0,0),
d(1997,10,26,6,0,0),
d(1998,4,5,7,0,0),
d(1998,10,25,6,0,0),
d(1999,4,4,7,0,0),
d(1999,10,31,6,0,0),
d(2000,4,2,7,0,0),
d(2000,10,29,6,0,0),
d(2001,4,1,7,0,0),
d(2001,10,28,6,0,0),
d(2002,4,7,7,0,0),
d(2002,10,27,6,0,0),
d(2003,4,6,7,0,0),
d(2003,10,26,6,0,0),
d(2004,4,4,7,0,0),
d(2004,10,31,6,0,0),
d(2005,4,3,7,0,0),
d(2005,10,30,6,0,0),
d(2006,4,2,7,0,0),
d(2006,10,29,6,0,0),
d(2007,3,11,7,0,0),
d(2007,11,4,6,0,0),
d(2008,3,9,7,0,0),
d(2008,11,2,6,0,0),
d(2009,3,8,7,0,0),
d(2009,11,1,6,0,0),
d(2010,3,14,7,0,0),
d(2010,11,7,6,0,0),
d(2011,3,13,7,0,0),
d(2011,11,6,6,0,0),
d(2012,3,11,7,0,0),
d(2012,11,4,6,0,0),
d(2013,3,10,7,0,0),
d(2013,11,3,6,0,0),
d(2014,3,9,7,0,0),
d(2014,11,2,6,0,0),
d(2015,3,8,7,0,0),
d(2015,11,1,6,0,0),
d(2016,3,13,7,0,0),
d(2016,11,6,6,0,0),
d(2017,3,12,7,0,0),
d(2017,11,5,6,0,0),
d(2018,3,11,7,0,0),
d(2018,11,4,6,0,0),
d(2019,3,10,7,0,0),
d(2019,11,3,6,0,0),
d(2020,3,8,7,0,0),
d(2020,11,1,6,0,0),
d(2021,3,14,7,0,0),
d(2021,11,7,6,0,0),
d(2022,3,13,7,0,0),
d(2022,11,6,6,0,0),
d(2023,3,12,7,0,0),
d(2023,11,5,6,0,0),
d(2024,3,10,7,0,0),
d(2024,11,3,6,0,0),
d(2025,3,9,7,0,0),
d(2025,11,2,6,0,0),
d(2026,3,8,7,0,0),
d(2026,11,1,6,0,0),
d(2027,3,14,7,0,0),
d(2027,11,7,6,0,0),
d(2028,3,12,7,0,0),
d(2028,11,5,6,0,0),
d(2029,3,11,7,0,0),
d(2029,11,4,6,0,0),
d(2030,3,10,7,0,0),
d(2030,11,3,6,0,0),
d(2031,3,9,7,0,0),
d(2031,11,2,6,0,0),
d(2032,3,14,7,0,0),
d(2032,11,7,6,0,0),
d(2033,3,13,7,0,0),
d(2033,11,6,6,0,0),
d(2034,3,12,7,0,0),
d(2034,11,5,6,0,0),
d(2035,3,11,7,0,0),
d(2035,11,4,6,0,0),
d(2036,3,9,7,0,0),
d(2036,11,2,6,0,0),
d(2037,3,8,7,0,0),
d(2037,11,1,6,0,0),
        ]

    _transition_info = [
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EWT'),
i(-14400,3600,'EPT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
i(-14400,3600,'EDT'),
i(-18000,0,'EST'),
        ]

Eastern = Eastern()

