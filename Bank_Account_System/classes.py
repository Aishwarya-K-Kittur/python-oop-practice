class BankAccount:
    bank_name = "State Bank of India"

    @classmethod
    def change_bank_name(cls, bank_name):
        cls.bank_name = bank_name

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance = self.__balance + amount
        else:
            print(f"Deposit amount is less than zero")

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance = self.__balance - amount
        else:
            print("Balance is less than withdrowal amount")

    def display(self):
        print("-------------------------")
        print(f"Bank: {self.bank_name}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance in the account: {self.__balance}")
        print("-------------------------")

    @staticmethod
    def is_valid_amount(amount):
        return amount > 0

    def get_balance(self):
        return self.__balance
    
    def set_balance(self, new_amount):
        if new_amount >= 0:
            self.__balance = new_amount
        else:
            print("Invalid balance")

account1 = BankAccount("Aishwarya", 1000)
account2 = BankAccount("Rahul", 5000)

account1.display()
account1.withdraw(100)
account1.display()
account1.deposit(300)
account1.display()

account1.withdraw(2000)

BankAccount.change_bank_name("Canara bank")
print(BankAccount.bank_name)
is_amount_valid = BankAccount.is_valid_amount(21)
print(f"Amount valid: {is_amount_valid}")

# print(account1._BankAccount__balance)    

print(f"balance left is {account1.get_balance()}")

account1.set_balance(0)
print(f"balance left is {account1.get_balance()}")


