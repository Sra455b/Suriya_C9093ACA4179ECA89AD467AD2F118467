class BankAccount:
  def __init__(self,account_number,account_holder_name,initial_balance=0.0):
    self.__account_number=account_number
    self.__account_holder_name=account_holder_name
    self.__account_balance=initial_balance

  def deposit(self,amount):
    if amount > 0:
      self.__account_balance += amount
      print("Deposited Rs{}. New Balance:Rs{}".format(amount,self.__account_balance ))
    else:
      print("Invalid deposit amount. Please deposit a positive amount.")
  def withdraw(self,amount):
    if amount > 0 and amount <= self.__account_balance:
      self.__account_balance -= amount
      print("Withdraw Rs{}. New balance: Rs {} ".format(amount,self.__account_balance))
  
    else:
      print("Invalid withdarwal amount or insufficient balnce.")

  def display_balance(self):
    print("Account balance for {} (Account #{}): Rs{}".format(self.__account_holder_name, self.__account_number, self.__account_balance))



account = BankAccount(account_number="1234567891",account_holder_name="Tony Stark",initial_balance=500000.0)


account.display_balance()
account.deposit(5000000000.0)
account.withdraw(100000)
account.display_balance()


      
