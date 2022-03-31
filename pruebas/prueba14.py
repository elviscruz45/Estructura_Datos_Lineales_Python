from functools import reduce

product = reduce((lambda x,y,z: x*y*z), [1,2,3,4,5,6])


print(product)
# Output: 24

def add(a, b):
    return a + b

print(reduce(add, [1, 2, 3, 4]))  # 10