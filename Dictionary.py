from collections import defaultdict

d = {'k1' : 1}
print(d['k1'])

d = defaultdict(object)
d['one']
for item in d:
    print(item)

b = defaultdict(lambda : 0)
b['one']
b['two'] = 2
