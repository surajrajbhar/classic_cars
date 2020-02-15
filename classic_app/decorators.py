
class Track_Calls:
    def __init__(self,f):
        self.f = f
        self.calls = 0
    
    def __call__(self,*args,**kargs):
        print(self.calls)  # bundle arbitrary arguments
        self.calls += 1
        return self.f(*args,**kargs)   # unbundle arbitrary arguments

    def called(self):
        return self.calls
    
    def reset_calls(self):
        self.calls = 0

@Track_Calls
def factorial(n):
    if n == 0:
        return 1
    else:
         return n*factorial(n-1)


print('hellpw orkd')