class Product:
    '''Inalizing'''
    __product_number = 0
    __total_money = 0
    def __init__(self, name, price, quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity
        Product.__product_number += 1
    
        
    '''funtion to get product number'''
    @classmethod
    def getProductNumber(cls):
        return Product.__product_number
    '''Get amount'''
    @property
    def getAmount(self):
        amount = self.__price * self.__quantity
        Product.__total_money += amount
        return amount
    
    @classmethod
    def getTotalMoney(cls):
        return Product.__total_money
    
    def output(self):
        print(f"Name: {self.__name}")
        print(f"Price: {self.__price}")
        print(f"Quantity: {self.__quantity}")
        print(f"Amount: {self.getAmount}")
        

    @staticmethod
    def getTotalAmount():
        return Product.__total_money
    
    
    