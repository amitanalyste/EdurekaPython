ans=(lambda z:z*4)
print(ans(7))

print("\n")
C = [39.2, 36.5, 37.3, 38, 37.8]
F = list(map(lambda x: (float(9)/5)*x + 32, C))
print(F)

#Map
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
print(squared)

#filter
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

#reduce
from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
print(product)