import random
from functools import reduce
class Array:
    def __init__(self,capacity,fill_value=None):
        self.items=list()
        for i in range(capacity):
            self.items.append(fill_value)

    def __len__(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
    def __iter__(self):
        return iter(self.items)
    
    def __getitem__(self,index):
        return self.items[index]
    
    def __setitem__(self,index,new_item):
        self.items[index]=new_item
        
    def __randReplace__(self):
        for i in range(len(self.items)):
            self.items[i]=random.randint(1,10)
            
    def __sum__(self):
        return reduce((lambda x,y:x+y),self.items)

print(next(Array(5).__iter__()))
print(next(Array(5).__iter__()))
print(next(Array(5).__iter__()))
print(next(Array(5).__iter__()))