from abc import ABCMeta, abstractmethod
from random import randint


class Account:
    @abstractmethod
    def create_account(self):
        return 0

    @abstractmethod
    def authenticate(self):
        return 0

    @abstractmethod
    def withdraw(self):
        return 0

    @abstractmethod
    def deposit(self):
        return 0

    @abstractmethod
    def display_balance(self):
        return 0


class SavingAccount(Account):
    def __init__(self):
        self.savingAccounts = {12345: ["ahmed", 200], 10002: ["salim", 350], 12354: ["ali", 1500]}

    def create_account(self, name, initial_deposit):
        self.account_number = randint(10000, 99999)
        self.savingAccounts[self.account_number] = [name, initial_deposit]
        print("\nYour account is successfully created, Your account number is {}\n".format(self.account_number))

    def authenticate(self, name, account_number):
        if account_number in self.savingAccounts.keys():
            if self.savingAccounts[account_number][0] == name:
                print("You have been authenticated successfully :) \n")
                self.account_number = account_number
                return True
            else:
                print("Wrong!, the name or the account number is wrong\n")
                return False
        else:
            print("Wrong!, the name or the account number is is wrong\n")
            return False

    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.savingAccounts[self.account_number][1]:
            print("You don't have all that money ")
            self.display_balance(self.account_number)
        else:
            self.savingAccounts[self.account_number][1] -= withdraw_amount
            print("Withdraw Successful\n")
            self.display_balance(self.account_number)

    def deposit(self, deposit_amount):
        self.savingAccounts[self.account_number][1] += deposit_amount
        print("Deposited Successfully\n")
        self.display_balance(self.account_number)

    def display_balance(self, account_number):
        print("Available balance: {}\n".format(self.savingAccounts[account_number][1]))


savingAccount = SavingAccount()

while True:
    user_choice = input("""Enter 1 to create a new account
Enter 2 to access an existing account
Enter 3 to exit
> """)
    if user_choice == '1':
        name = input("Enter your name: ")
        while name == "":
            name = input("Enter your name: ")
        user_input = input("Enter an initial deposit: ")
        while not user_input.isdigit():
            user_input = input("Wrong input type, deposit should be a number, try again: ")
        initial_deposit = int(user_input)

        savingAccount.create_account(name, initial_deposit)

    elif user_choice == '2':
        auth = False
        name = input("Enter the name: ")
        user_input = input("Enter the account number: ")
        while not user_input.isdigit():
            user_input = input("Wrong input type, the account number should be a number, try again: ")
        accountNumber = int(user_input)
        while not savingAccount.authenticate(name, accountNumber):
            if input("press q to quit, or anything to continue > ") == "q":
                break
            name = input("Enter the name: ")
            user_input = input("Enter the account number: ")
            while not user_input.isdigit():
                user_input = input("Wrong input type, the account number should be a number, try again: ")
            accountNumber = int(user_input)
        else:
            auth = True
        while auth:
            user_choice = input(f"""Enter 1 to withdraw"
Enter 2 to deposit
Enter 3 to display balance
Enter 4 to exit
> """)
            if user_choice == '1':
                user_input = input("Enter withdraw amount : ")
                while not user_input.isdigit():
                    user_input = input("Wrong input type, the withdraw amount should be a number, try again: ")
                withdrawAmount = int(user_input)
                savingAccount.withdraw(withdrawAmount)
            elif user_choice == '2':
                user_input = input("Enter deposit amount : ")
                while not user_input.isdigit():
                    user_input = input("Wrong input type, the deposit amount should be a number, try again: ")
                deposit_amount = int(user_input)
                savingAccount.deposit(deposit_amount)
            elif user_choice == '3':
                savingAccount.display_balance(accountNumber)
            elif user_choice == '4':
                break
            else:
                print("I don't understand !!\n")
    elif user_choice == '3':
        quit()
    else:
        print("I don't understand !!\n")
