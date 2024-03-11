import math

class Calculator:
    def __init__(self,num):
        self.num = num
    
    def __add__(self,n):
        return self.num + n
    
    def __sub__(self,n):
        return self.num - n
    
    def __multiply__(self,n):
        return self.num * n
    
    def __exponent__(self,n):
        return self.num**n
    
    def __div__(self,n):
        if n == 0:
            print("Can't divide by zeo")
        else:
            return self.num/n
        
N = Calculator(10)
print(N + 5)