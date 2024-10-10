def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)

print(f(0))



def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs
f('spam')


# !a   ->  ascii()
# !r   -> repr()
# !s   -> str()
animals = 'eels'
print(f'My hovercraft is full of {animals}.')
# My hovercraft is full of eels.
print(f'My hovercraft is full of {animals!r}.')
# My hovercraft is full of 'eels'.

bugs = 'roaches'
count = 13
area = 'living room'
print(f'Debugging {bugs=} {count=} {area=}')
# Debugging bugs='roaches' count=13 area='living room'