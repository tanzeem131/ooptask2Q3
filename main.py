class ACCOUNT:
    def __init__(self,Account_No, Account_holder_name,Amount):
        self.Account_No = Account_No
        self.Account_holder_name = Account_holder_name
        self.Amount = Amount

    def displaydetails(self):
        print("Account_No:",self.Account_No,"Account_holder_name:",self.Account_holder_name,"Amount:",self.Amount)

    def deposit(self):
        amount = float(input("Deposited amount: "))
        self.Amount += amount
        print("\n Amount Deposited:", amount)

    def withdraw(self):
        amount = float(input("Withdrawn amount: "))
        if self.Amount >= amount:
            self.Amount -= amount
            print("\n Amount Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
    def display(self):
        print("\n Net Balance=", self.Amount)
person = ACCOUNT(123456789012,'Tanzeem',5000)
person.displaydetails()
person.deposit()
person.withdraw()
person.display()

