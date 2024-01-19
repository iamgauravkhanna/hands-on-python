import collections

order_dic = collections.OrderedDict()
order_dic['A'] = 10
order_dic['C'] = 12
order_dic['B'] = 11
order_dic['D'] = 13

for k, v in order_dic.items():
    print(k, v)