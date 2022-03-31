class classA():
    
    def __init__(self):
        self.var1 = 0
        self.var2 = "Hello"

    def __repr__(self):
        return "This is object of class Aaaa"

    def __str__(self):
        '''print("var1 =", self.var1)
        print("var2 =", end="ddd ")'''
        return self.var2

A = classA()
print(A)