class BankAccount: 
    

    def __init__(self, name, balance, interest_rate) -> None:
        self.name = name
        self.account_balance = balance
        self.interest_rate = interest_rate
        self.total_interest_earned = 0

    def balance(self): return self.account_balance
    
    def rename(self):
        self.name = input("Choose a new name for this account: ")
        print("Success. This account's new name is: {0}".format(self.name))


    def deposit(self, amount):
        self.account_balance += amount
        print("Successfully deposited {0} into your account. \nYour new balance is: {1}".format(amount, self.account_balance))

    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            print("Successfully withdrew {0} from your account. \nYour new balance is: {1}".format(amount, self.account_balance))
        else: print("You do not have enough money to cover this withdrawal.")

    def interest(self, years):
        differential = self.account_balance
        self.account_balance *= ((1+(self.interest_rate / 100)) ** years)
        self.total_interest_earned += (eval(str(self.account_balance - differential)))
        print("{0}% Interest applied over {1} Years. New balance: {2}".format(self.interest_rate, years, self.account_balance))

    def open_savings(self):
        answer = input("Confirm the opening of a new savings account? (YES/NO) ")
        if answer == "YES" or answer == "yes":
            self.savings_balance = 0
            print("You have successfully opened a savings account. Balance: " + str(self.savings_balance))

        else:
            print("You have successfully cancelled opening a savings account.")

    def savings_exists(self) -> bool:
        if hasattr(self, 'savings_balance'):
            return True

    
    def save(self, amount):
        if self.savings_exists == True:
            if amount <= self.account_balance:
                self.account_balance -= amount
                self.savings_balance += amount
                print("\nSuccessfully deposited {0} into savings. \nYour savings balance is: {1}\nYour account balance is: {2}\n".format(amount, self.savings_balance, self.account_balance))
            else: print("You do not have enough to deposit this amount into savings.")
        else: 
            answer = input("\nYou don't have a savings to deposit to.\nWould you like to open a new savings account? (YES/NO) ")
            if answer == "YES" or answer == "yes":
                self.open_savings()
            else: print("You chose not to open a savings account.")

    def transfer(self, recipient, amount):
        if isinstance(recipient, BankAccount):
            if amount <= self.account_balance: 
                recipient.deposit(amount)
                self.withdraw(amount)
            else: print("Not enough money to make this transfer. ")
        else: print("This user is not a member of the bank.")


    def info(self) -> None:
        print("\n====ACCOUNT INFO====\n")
        print("Account Name: " + self.name)
        print("Account Balance: " + str(self.account_balance))
        print("Account Interest Rate: " + str(self.interest_rate) + "% APR")
        if self.savings_exists == True: 
            print("Savings Exists: YES")
            print("Savings Balance: " + str(self.savings_balance))
        else: print("Savings Exists: NO")
        print("Lifetime Interest Gained: " + str(self.total_interest_earned))
        print("\n====================\n")







    
Draco = BankAccount("Draco", 500, 5)
John = BankAccount("John", 500, 0)

print(BankAccount)




