class BankAccount:
    def __init__(self, initial_balance):
        """Creates an account with the given balance."""
        self.initial_balance = initial_balance 
        self.fees = 0
        self.credit = 0

    def deposit(self, amount):
        """Deposits the amount into the account."""
        self.amount = amount
        
        if (self.initial_balance + self.amount) == 0:
            self.fees += 5
        
        if self.initial_balance < 0:
            self.credit = 5
            self.fees += 5
        else:
            self.credit = 0 
              
        self.initial_balance = self.initial_balance + self.amount - self.credit
                      
        print self.initial_balance, self.fees
            
    def withdraw(self, amount):
        """
        Withdraws the amount from the account. Each withdrawal 
        resulting in a negative balance also deducts a penalty 
        fee of 5 dollars from the balance.
        """
        self.amount = amount
        
        if (self.initial_balance - self.amount) == 0:
            self.fees += 5
        
        if self.initial_balance < 0:
            self.credit = 5
            self.fees += 5
        else:
            self.credit = 0 
              
        self.initial_balance = self.initial_balance - self.amount - self.credit
                      
        print self.initial_balance, self.fees
        
    def get_balance(self):
        """Returns the current balance in the account."""
        return self.initial_balance

    def get_fees(self):
        """Returns the total fees ever deducted from the account."""
        return self.fees
        
        
#my_account = BankAccount(10)
#my_account.withdraw(15)
#my_account.deposit(20)
#print my_account.get_balance(), my_account.get_fees()

my_account = BankAccount(10)
my_account.withdraw(5)
my_account.deposit(10)
my_account.withdraw(5)
my_account.withdraw(15)
my_account.deposit(20)
my_account.withdraw(5)
my_account.deposit(10)
my_account.deposit(20)
my_account.withdraw(15)
my_account.deposit(30)
my_account.withdraw(10)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(50)
my_account.deposit(30)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5)
my_account.deposit(20)
my_account.withdraw(15)
my_account.deposit(10)
my_account.deposit(30)
my_account.withdraw(25)
my_account.withdraw(5)
my_account.deposit(10)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(10)
my_account.withdraw(15)
my_account.deposit(10)
my_account.deposit(30)
my_account.withdraw(25)
my_account.withdraw(10)
my_account.deposit(20)
my_account.deposit(10)
my_account.withdraw(5)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5)
print my_account.get_balance(), my_account.get_fees()