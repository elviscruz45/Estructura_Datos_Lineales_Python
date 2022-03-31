
def iter(num):
    n=-1
    while n<5:
        n+=1
        yield n
        
        
num=[1,2,3,4,5,6,7,8,9]


print(next(iter(num)))

print(next(iter(num)))

print(next(iter(num)))

'''

def iter():
    n=1
    num=[1,2,3,4,5,6,7,8,9]

    while n<10:
        n+=1
        yield num**2
'''



def square(nums):
    for i in nums:
        yield(i*i)

someNums = square([1, 2, 3, 4, 5])

print (someNums)
print (next(someNums))
print (next(someNums))
print (next(someNums))
print (next(someNums))
