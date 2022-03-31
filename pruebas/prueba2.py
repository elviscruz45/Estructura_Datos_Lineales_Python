class Students(object):
    def __init__(self, *args):
        self.names = args
    def __len__(self):
        return len(self.names)
    
    

ss = Students('Bob', 'Alice', 'Tim')
print(len(ss))
