class Finance:
    def __init__(self):
        self.__revenue = 100000      #private data
        self.__number_of_sales = 100  #private data

    def display(self):
        print(f'revenue is {self.__revenue} and number of sales is {self.__number_of_sales}')

f1 = Finance()
f1.display()

        

