'''
class vector(object):
     
    def __init__(self, vector):
        self.vector=vector
 
    def __getitem__(self,n):
        return self.vector[n]
 
u=vector([1,2,3])
print (u[2])
'''
'''

class matriz(object):
     
    def __init__(self,matriz):
        self.matriz=matriz
 
    def __getitem__(self, i, j):
        return self.matriz[i][j]
 
A=matriz([[1,1,1],[1,1,1],[1,1,1]])
print (A[1][2])
'''

'''
class matriz(object):
 
    def __init__(self,matriz):
        self.matriz=matriz
 
    def __getitem__(self, nums):
        i, j = nums
        return self.matriz[i][j]
 
A=matriz([[1, 3, 5],[2, 4, 6],[7, 9, 11]])
print (A[1, 2])
'''

'''
class matriz(object):
     
    def __init__(self,matriz):
        self.matriz=matriz
 
    def __getitem__(self, i, j):
        return self.matriz[i][j]
 
A=matriz([[1, 3, 5],[2, 4, 6],[7, 9, 11]])
print (A.__getitem__(1,2))

'''

class matriz(object):
     
    def __init__(self, matriz):
        self.matriz= matriz
 
    def __getitem__(self, item):
        return self.matriz[item]
 
A= matriz([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(A[1][2]) #6
