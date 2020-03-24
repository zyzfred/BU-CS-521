class Account:

  # constructor
  def __init__(self):
    self.id = int(0)
    self.balance = float(100)
    self.annualInterestRate = float(0)

  # accessor
  def getID(self):
    return self.id
  
  def getBalance(self):
    return self.balance

  def getAnnualInterestRate(self):
    return self.annualInterestRate

  # mutator
  def modifyID(self, newID: int):
    self.id = newID

  def modifyBalance(self, newBalance: float):
    self.balance = newBalance
  
  def modifyAnnualInterestRate(self, newAnnualInterestRate: float):
    self.annualInterestRate = newAnnualInterestRate

  # other functions
  def getMonthlyInterestRate(self):
    return self.annualInterestRate / 12
  
  def getMonthlyInterest(self):
    return self.balance * self.getMonthlyInterestRate() / 100

  def withdraw(self, amount: float):
    self.balance -= amount

  def deposit(self, amount: float):
    self.balance += amount

# test out
Account1 = Account()
Account1.modifyID(1122)
Account1.modifyBalance(20000)
Account1.modifyAnnualInterestRate(4.5)
Account1.withdraw(2500)
Account1.deposit(3000)
print('Account id: ' + str(Account1.getID()))
print('Account balance: ' + str(Account1.getBalance()))
print('Account monthly interest rate: ' + str(Account1.getMonthlyInterestRate()))
print('Account monthly interest: ' + str(Account1.getMonthlyInterest()))