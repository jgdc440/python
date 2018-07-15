s = set([1, 2, 3])
t = set([2, 3, 4])
r = s
print r
s.intersection_update(t)
print s
q = s.union(r)
print q