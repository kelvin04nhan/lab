class Account:
    def __init__(self, number, balance):
        if not isinstance(number, int):
            raise TypeError('number should be type int ')
        if not isinstance(balance, float):
            raise TypeError('Balance should be double')
        
        self.number = number
        self.balance = balance
        
    def getNumber(self):
        return self.number
      
    def getBalance(self):
        return self.balance
    
    def __str__(self):
        return f"Account[number ={self.number}, balance = ${self.balance}]"
    
    def credit(self, amount):
        # if isinstance(amount, float):
        self.balance += amount
            
        # else:
        #     print('Invalid amount type. Please provide a float value.')       
                    
    def debit(self, amount):
        # if isinstance(amount, float):
        if self.balance >= amount:
            self.balance -= amount
        #     else: print('Amount exceeded')
        # else:
        #     print('Invalid amount type. Please provide a float value.')        
            
    def transferTo(self, destination_account, amount):
        if not isinstance(destination_account, Account):
            raise TypeError('Destination account should be subclass of Account')
        if isinstance(amount, (int, float)):
            if self.balance >= amount:
                self.balance -= amount
                destination_account.credit(amount)
                print(f"{self.number} transferred to {destination_account.getNumber()}: ${amount}")
            else:
                    print('Insufficient funds')
        else:
                print('Invalid amount type. Please provide an int or float value.')
