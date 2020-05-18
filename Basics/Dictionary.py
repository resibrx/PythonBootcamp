from collections import defaultdict
from collections import OrderedDict
#defaultdict
d = {'k1' : 1}
print(d['k1'])

d = defaultdict(object)
d['one']
for item in d:
    print(item)

b = defaultdict(lambda : 0)
b['one']
b['two'] = 2

#ordereddict
x = OrderedDict()
x['a'] = 1
x['b'] = 2
x['c'] = 3
x['d'] = 4

for k,v in d.items():
    print(k,v)
