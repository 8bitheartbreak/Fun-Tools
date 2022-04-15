import time
import sys


class Account:

    Customers = []



    def create_account(self, accountName, accountBalance, accountType):
        self.accountBalance = accountBalance
        self.accountName = accountName
        self.accountType = accountType
        return accountName, accountBalance, accountType
        print("\n\nCreated", self.accountType, "account for ", str(accountName))
        print("Starting account balance is: $", str(accountBalance))


class CheckingAccount(Account):

    def create_checking(self, accountName, accountBalance):
        self.accountBalance = accountBalance
        self.accountName = accountName
        self.accountType = "Checking"
        print("\n\nCreated account for ", str(accountName))
        print("Starting account balance is: $", str(accountBalance))

    def add_money(self, amount):
        self.accountBalance += amount
        print("\nyou added ${0} to your Bank, {1}".format(str(amount), str(self.accountName)))
        print("Your account balance is: $" + str(self.accountBalance))

    def withdraw_money(self, amount):
        if amount <= self.accountBalance:
            self.accountBalance -= amount
            print("\nyou withdrew ${0} from your Bank, {1}".format(str(amount), str(self.accountName)))
            print("Your account balance is: $", str(self.accountBalance))
        else:
            print("\nInsufficient funds for withdrawal!")
            print("Your account balance is: $", str(self.accountBalance))

    def info(self):
        print("\nAccount Information: \n", self.accountName)
        print(self.accountBalance)
        print(self.accountType)


class SavingAccount:

    def __init__(self, accountNameArgs, accountBalanceArgs, yearlyAprArgs):
        self.accountType = "Savings"
        self.accountBalance = accountBalanceArgs
        self.accountName = accountNameArgs
        self.yearlyApr = yearlyAprArgs
        print("\n\nCreated savings account for ", str(self.yearlyApr),
              " with starting balance " + str(self.accountBalance))
        print(messages['bal'], str(self.accountBalance))

    def add_money(self, amount):
        self.accountBalance += amount
        print("\nyou added ${0} to your Bank, {1}".format(str(amount), str(self.accountName)))
        print(messages['bal'], str(self.accountBalance))

    def gain_interest(self, yrs):
        if self.yearlyApr > 0:
            balance = self.accountBalance
            self.accountBalance *= ((self.yearlyApr / 100) + 1) ** yrs
            interest = round(self.accountBalance - balance, 2)
            print("\nYour interest has been applied! New balance: ",
                  str((round(self.accountBalance, 2))))
            print("Years stored: {0} \nAPR: {1}%/yr\nEarned interest: ${2}".
                  format(str(yrs), str(self.yearlyApr / 100), str(interest)))
        else:
            print("Yearly APR isn't positive!")
    def info(self):
        print("\nAccount Information: \n", self.accountName)
        print("$" + str(round(self.accountBalance, 2)))
        print(self.accountType)



messages = {
    'deposit': "\nyou added ${0} to your Bank, {1}",
    'withdraw': "\nYou withdrew ${0} from your Bank, {1}",
    'create': "\n\nCreated account for ",
    'bal': "\nYour account balance is: $"
}


#class Bank():

    #def createChecking(self, name, balance):
        #CheckingAccount(name, balance)

    #def createSaving(self):
      #  pass

   # def list(self):
        #accountList = []
        #accountList.append(CheckingAccount().accountName)


bob = CheckingAccount().create_account("Bob", 30, )
# bob.add_money(50)
# bob.withdraw_money(80)
# bob.info()





