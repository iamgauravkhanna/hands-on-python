import collections

d1 = collections.OrderedDict()
d1['A'] = 10
d1['C'] = 12
d1['B'] = 11
d1['D'] = 13

for k, v in d1.items():
    print(k, v)