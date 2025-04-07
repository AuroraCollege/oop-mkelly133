class BankAcct:
    def __init__(self, account_number, account_holder, balance, pin):
        self.account_number = account_number # Public
        self.account_holder = account_holder
        self.__balance = balance #Private
        self.__pin = pin

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self,amount,pin):
        if self.pin == pin and self.balance >= amount:
            self.__balance -= amount

