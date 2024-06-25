class Cart:
    def __init__(self, bsk1,bsk2,bsk3):
        self.clothes = bsk1
        self.gadgets = bsk2
        self.furniture = bsk3

    def __len__(self):
        print('total number of items in cart:')
        return len(self.clothes)+len(self.gadgets)+len(self.furniture)
        


customer = Cart(['Jeans','T-shirt', 'Shirt'],['Mobile', 'Earbuds'],['Table','Chair'])
print(len(customer))
