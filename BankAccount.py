class BankAccount(object):
  balance = 0

  def __init__(self,name):
    self.name = name

  def __repr__(self):
    return "%s's account. Balance $%.2f" % (self.name, self.balance)

  def show_balance(self):
    return "You have $%.2f in your account" % (self.balance)
    
  def deposit(self, amount):
    self.amount = amount
    if self.amount <= 0:
      print "Invalid deposit amount"
      return
    else:
      print "$%.2f is deopsited" % (self.amount)
      self.balance += self.amount
      self.show_balance()

  def withdraw(self, amount):
    self.amount = amount
    if self.amount > self.balance:
      print "Invalid withdraw amount"
      return
    else:
      self.balance -= self.amount
      print "$%.2f is withdraw" % (self.amount)
      self.show_balance
    
my_account = BankAccount("sai")
print(my_account)
print(my_account.show_balance())
my_account.deposit(2000)
my_account.withdraw(1000)
print(my_account)

