class BankAccount :
    def __init__(self, account_number, balance=0) :
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.amount = amount
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            print("Balance is sufficient")

        if self.balance >= amount:
            return amount - self.balance
        
        if amount >= self.balance:
            print("Transaction failed as balance is insufficient")


    def get_balance(self):
        current_balance = self.amount - self.balance
        return current_balance

        print(current_balance)
    BankAccount()   
    bank1 = BankAccount(123456789)
    deposit()
    withdraw()
    print(get_balance)
