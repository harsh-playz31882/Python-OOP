class Finance:
    def __init__(self):
        self.__revenue=100000  #private data
        self.number_of_sales=120 
        

f1 = Finance()


class HR():
    def __init__(self):
        self.number_of_employee=64
        print(f1.revenue)  # attribute error will come as we cant modify, private data

h1 = HR()
print(f1.__dict__)
