#!/usr/bin/env python
import mincemeat
import sys
# Don't forget to start a client!
# ./mincemeat.py -l -p changeme

hash_k = ''

if len(sys.argv) == 2:
  hash_k = sys.argv[1]

print 'Attacking ' + hash_k
import itertools
l1 = list(itertools.product('abcdefghijklmnopqrstuvwxyz0123456789', repeat=1))
l2 = list(itertools.product('abcdefghijklmnopqrstuvwxyz0123456789', repeat=2))
l3 = list(itertools.product('abcdefghijklmnopqrstuvwxyz0123456789', repeat=3))
l = l1+l2+l3

temp = ''
counter = 0
datasource = {}
for line in l:
  temp = temp + ''.join(line) + ' '
  if counter % 600 == 0:
    temp = temp + hash_k
    datasource[counter] = temp
    temp = ''
  counter += 1
datasource[counter] = temp

def mapfn(k, v):
    ll = 'abcdefghijklmnopqrstuvwxyz0123456789'
    ppp = v.split()
    hhh = ppp[-1]

    for n in ppp:
        import hashlib
        if len(n) == 3:
            for g in ll:
                ta = n + g
                hval = hashlib.md5(ta).hexdigest()
                if hval[:5] == hhh:
                    yield ta,1
        hval = hashlib.md5(n).hexdigest()
        if hval[:5] == hhh:
            yield n,1
          


def reducefn(k, vs):
    return vs

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

matchlist = s.run_server(password="changeme")

print matchlist.keys()

