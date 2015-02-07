#!/usr/bin/env python2.3

"""Parse the BLATHER logging generated by ZEO2.

An example of the log format is:
2002-04-15T13:05:29 BLATHER(-100) ZEO Server storea(3235680, [714], 235339406490168806) ('10.0.26.30', 45514)
"""

import re
import time

rx_time = re.compile('(\d\d\d\d-\d\d-\d\d)T(\d\d:\d\d:\d\d)')

def parse_time(line):
    """Return the time portion of a zLOG line in seconds or None."""
    mo = rx_time.match(line)
    if mo is None:
        return None
    date, time_ = mo.group(1, 2)
    date_l = [int(elt) for elt in date.split('-')]
    time_l = [int(elt) for elt in time_.split(':')]
    return int(time.mktime(date_l + time_l + [0, 0, 0]))

rx_meth = re.compile("zrpc:\d+ calling (\w+)\((.*)")

def parse_method(line):
    pass

def parse_line(line):
    """Parse a log entry and return time, method info, and client."""
    t = parse_time(line)
    if t is None:
        return None, None
    mo = rx_meth.search(line)
    if mo is None:
        return None, None
    meth_name = mo.group(1)
    meth_args = mo.group(2).strip()
    if meth_args.endswith(')'):
        meth_args = meth_args[:-1]
    meth_args = [s.strip() for s in meth_args.split(",")]
    m = meth_name, tuple(meth_args)
    return t, m

class TStats:

    counter = 1

    def __init__(self):
        self.id = TStats.counter
        TStats.counter += 1

    fields = ("time", "vote", "done", "user", "path")
    fmt = "%-24s %5s %5s %-15s %s"
    hdr = fmt % fields

    def report(self):
        """Print a report about the transaction"""
        t = time.ctime(self.begin)
        if hasattr(self, "vote"):
            d_vote = self.vote - self.begin
        else:
            d_vote = "*"
        if hasattr(self, "finish"):
            d_finish = self.finish - self.begin
        else:
            d_finish =  "*"
        print self.fmt % (time.ctime(self.begin), d_vote, d_finish,
                          self.user, self.url)

class TransactionParser:

    def __init__(self):
        self.txns = {}
        self.skipped = 0

    def parse(self, line):
        t, m = parse_line(line)
        if t is None:
            return
        name = m[0]
        meth = getattr(self, name, None)
        if meth is not None:
            meth(t, m[1])

    def tpc_begin(self, time, args):
        t = TStats()
        t.begin = time
        t.user = args[1]
        t.url = args[2]
        t.objects = []
        tid = eval(args[0])
        self.txns[tid] = t

    def get_txn(self, args):
        tid = eval(args[0])
        try:
            return self.txns[tid]
        except KeyError:
            print "uknown tid", repr(tid)
            return None

    def tpc_finish(self, time, args):
        t = self.get_txn(args)
        if t is None:
            return
        t.finish = time

    def vote(self, time, args):
        t = self.get_txn(args)
        if t is None:
            return
        t.vote = time

    def get_txns(self):
        L = [(t.id, t) for t in self.txns.values()]
        L.sort()
        return [t for (id, t) in L]

if __name__ == "__main__":
    import fileinput

    p = TransactionParser()
    i = 0
    for line in fileinput.input():
        i += 1
        try:
            p.parse(line)
        except:
            print "line", i
            raise
    print "Transaction: %d" % len(p.txns)
    print TStats.hdr
    for txn in p.get_txns():
        txn.report()
