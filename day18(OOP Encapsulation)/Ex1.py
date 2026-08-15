class Bankaccount:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.__balance=balance
    def get_balance(self):
        return self.__balance
    def deposit(self,amount):
        self.amount=amount
        self.__balance=amount+self.__balance
    def withdraw(self,amount):
        self.amount=amount
        if self.amount<self.__balance:
            self.__balance=self.__balance-amount
        else:
           print("Not enough money to withdraw")

        

bank=Bankaccount("Pooja",1000)
bank.deposit(300)
print(bank.get_balance())
bank.withdraw(300)
print(bank.get_balance())
bank.withdraw(3000)
print(bank.get_balance())

    

