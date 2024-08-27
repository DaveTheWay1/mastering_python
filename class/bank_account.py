import random

class BankAccount():
  def __init__(self, owner, balance, has_overdraft = False):
    self.owner = owner
    self.balance = balance
    self.has_overdraft = has_overdraft
    self.account_no = random.randint(111111111, 999999999)

  def deposit(self,amount):
    self.balance += amount
    print(f"You desposited {amount} bringing a new total balance of ${self.balance}")

  def withdraw(self,amount):
    if self.balance < amount and self.has_overdraft == True or self.balance > amount:
      self.balance -= amount
      print(f"You withdrew {amount} bringing a new total balance of ${self.balance}")
    else: 
      print("Withdraw not permitted as has_overdraft is false. Please set to true for this transaction")

  def __str__(self):
    return f"Account: {self.account_no} / Balance: {self.balance}"
  

David = BankAccount("David", 15.00)
print(David)
David.withdraw(4)
David.deposit(50)
David.withdraw(100)

David = BankAccount("David", 15.00, True)
print(David)
David.withdraw(4)
David.deposit(50)
David.withdraw(100)

# output:
# Account: 364968859 / Balance: 15.0
# You withdrew 4 bringing a new total balance of $11.0
# You desposited 50 bringing a new total balance of $61.0
# Insufficient funds. Please try again

class SavingsAccount():
  def __init__(self, owner, balance,):
    BankAccount.__init__(self, owner, balance)
  
  def withdraw(self):
    return "No withdrawls permitted"
  

David_Savings = SavingsAccount("David", David.balance)
print(David_Savings.withdraw())
# * No withdrawls permitted
