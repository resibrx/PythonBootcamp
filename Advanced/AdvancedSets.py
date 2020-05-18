myset = set()
myset.add(1)
myset.add(2)
myset.add(2)
print(myset)
myset.clear()

anotherset = {1,2,3}
anotherset.add(4)

#difference method
myset.difference(anotherset)

s1 = {1,2,3}
s2 = {4,5,6}
s1.difference_update(s2)
