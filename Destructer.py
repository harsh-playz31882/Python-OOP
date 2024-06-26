import time
class NegetiveAge(Exception):
    pass

class Age:
    def __init__(self, age):
        if age<0:
            raise NegetiveAge('Age cannot be negetive')
        
    def __del__(self):
        print('destructor is called')
    
ag = Age(-10)
print(ag)
time.sleep(5)