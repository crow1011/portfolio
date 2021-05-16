# is - identical
# == - equal

a = [1, 2, 3, ]
b = a
c = [1, 2, 3, ]

# True: a == b
print('a == b', a == b)
# True: a == c
print('a == c', a == c)

# True: a is b
print('a is b', a is b)
# False: a is c
print('a is c', a is c)
