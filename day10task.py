class  bank_Account:
    def __init__(self):
        self.balance = 0
        print("hello!!! welcome to the deposit & Withdrawal Machine")

class Deposit(bank_Account):
    def deposit(self):
        amount = float(input("Enter amount to be Deposit:"))
        self.balance = self.balance + amount
        print("\n amount deposited:",amount)
class Withdraw(Deposit):
    def withdraw(self):
        money =float(input("Enter amount to be Withdrawn:"))
        self.balance>=money
        self.balance = self.balance - money
        print("\n you Withdraw:",money)
    def display(self):
        print("\n Net Available Balance=", self.balance)



m = Deposit()
m.deposit()
q = Withdraw()
q.withdraw()
q.display()