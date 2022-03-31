def my_generator():
    
    x = 1
    print("new value is generated!")
    yield x
    x = x + 1
    print("new value is generated!")
    yield x
    x = x + 1
    print("new value is generated!")
    yield x
    
    x = x + 1
    print("new value is generated!")
    yield x
    
    x = x + 1
    print("new value is generated!")
    yield x
    

print(my_generator())

'''
gen_iter = my_generator()
for val in gen_iter:
    print("Value =", val)  '''
    
    
print(next(my_generator()))
