
def iter():
    n=4
    num=[1,2,3,4,5,6,7,8,9]
    while n<10:
        n+=1
        yield num[n]
        
        
    


print(next(iter()))

print(next(iter()))

print(next(iter()))

'''

def iter():
    n=1
    num=[1,2,3,4,5,6,7,8,9]

    while n<10:
        n+=1
        yield num**2
'''