from collections import namedtuple

t = (1,2,3)
#grab first element
print(t[0])

#assigned named as well as numeral index
Dog = namedtuple('Dog', 'age breed name')
sam = Dog(age=2,breed='Lab',name='Sam')
print(sam)
print(sam.age)
print(sam[0])

Cat = namedtuple('Cat', 'fur claws name')
kitty = Cat(fur='fuzzy', claws=False, name='Kitty')
print(kitty)
