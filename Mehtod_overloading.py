class Calc:
    def add(self, num1=None, num2=None, num3=None):
        if num1 != None and num2 != None and num3 != None:
            print(num1+num2+num3)
        elif num1 != None and num2 != None:
            print(num1 + num2)
        else:
            print('incorrect parameter')


       

        

        

c1 = Calc ()
c1.add(10,20)
c1.add(10,20,30)
    



