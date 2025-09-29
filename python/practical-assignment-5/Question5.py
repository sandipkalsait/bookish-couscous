
class Account:
    bank_name = "SK_Bank"
    currency = "INR"
    # 
    minimum_balance = 1000

    def __init__(self, account_number, holder_name, account_type, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"{Account.currency} {amount} deposited successfully. New balance: {Account.currency} {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if self.balance - amount < Account.minimum_balance:
            print(f"Cannot withdraw {Account.currency} {amount}. Minimum balance of {Account.currency} {Account.minimum_balance} must be maintained.")
            return
        self.balance -= amount
        print(f"{Account.currency} {amount} withdrawn successfully. New balance: {Account.currency} {self.balance}")

    def balance_enquiry(self):
        print(f"Current balance: {Account.currency} {self.balance}")

    def display_details(self):
        print(f"""
        Bank Name       : {Account.bank_name}
        Account Number  : {self.account_number}
        Account Holder  : {self.holder_name}
        Account Type    : {self.account_type}
        Balance         : {Account.currency} {self.balance}
        """)


class Bank:
    account_types = ["Savings", "Current"]

    def __init__(self):
        self.accounts = []

    def find_account(self, account_number):
        for acc in self.accounts:
            if acc.account_number == account_number:
                return acc
        return None

    def open_account(self):
        while True:
            account_number = input("Enter Account Number (numeric): ").strip()
            if not account_number.isdigit():
                print("Account number must be numeric.")
                continue
            if self.find_account(account_number):
                print("Account number already exists!")
                continue
            holder_name = input("Enter Account Holder Name: ").strip()
            if not holder_name.replace(" ", "").isalpha():
                print("Invalid name. Only letters allowed.")
                continue
            print("Account Types:", ", ".join(Bank.account_types))
            account_type = input("Enter Account Type: ").strip()
            if account_type not in Bank.account_types:
                print("Invalid account type.")
                continue
            balance_input = input(f"Enter opening balance (minimum {Account.minimum_balance}): ").strip()
            if not balance_input.isdigit() or int(balance_input) < Account.minimum_balance:
                print(f"Opening balance must be numeric and at least {Account.minimum_balance}.")
                continue
            account = Account(account_number, holder_name, account_type, int(balance_input))
            self.accounts.append(account)
            print(f"Account {account_number} opened successfully.")
            more = input("Want to open another account? YES/NO: ").strip().lower()
            if more != 'yes':
                break

    def deposit(self):
        while True:
            account_number = input("Enter Account Number to deposit: ").strip()
            account = self.find_account(account_number)
            if not account:
                print("Account not found!")
                more = input("Try another account? YES/NO: ").strip().lower()
                if more != 'yes':
                    break
                continue
            amount_input = input("Enter deposit amount: ").strip()
            if not amount_input.isdigit():
                print("Amount must be numeric.")
                continue
            account.deposit(int(amount_input))
            more = input("Deposit to another account? YES/NO: ").strip().lower()
            if more != 'yes':
                break

    def withdraw(self):
        while True:
            account_number = input("Enter Account Number to withdraw: ").strip()
            account = self.find_account(account_number)
            if not account:
                print("Account not found!")
                more = input("Try another account? YES/NO: ").strip().lower()
                if more != 'yes':
                    break
                continue
            amount_input = input("Enter withdrawal amount: ").strip()
            if not amount_input.isdigit():
                print("Amount must be numeric.")
                continue
            account.withdraw(int(amount_input))
            more = input("Withdraw from another account? YES/NO: ").strip().lower()
            if more != 'yes':
                break

    def balance_enquiry(self):
        while True:
            account_number = input("Enter Account Number for balance enquiry: ").strip()
            account = self.find_account(account_number)
            if not account:
                print("Account not found!")
                more = input("Try another account? YES/NO: ").strip().lower()
                if more != 'yes':
                    break
                continue
            account.balance_enquiry()
            more = input("Check another account? YES/NO: ").strip().lower()
            if more != 'yes':
                break

    def display_account(self):
        while True:
            account_number = input("Enter Account Number to display details: ").strip()
            account = self.find_account(account_number)
            if not account:
                print("Account not found!")
                more = input("Try another account? YES/NO: ").strip().lower()
                if more != 'yes':
                    break
                continue
            account.display_details()
            more = input("Display another account? YES/NO: ").strip().lower()
            if more != 'yes':
                break

    def menu(self):
        while True:
            print("""
            #------------- Bank Account Menu -----------#
            1. Open Account
            2. Deposit
            3. Withdraw
            4. Balance Enquiry
            5. Display Account Details
            0. Exit
            """)
            choice = input("Enter your choice: ").strip()
            if not choice.isdigit():
                print("Please enter a number.")
                continue
            choice = int(choice)
            if choice == 0:
                print("Exiting program...")
                break
            elif choice == 1:
                self.open_account()
            elif choice == 2:
                self.deposit()
            elif choice == 3:
                self.withdraw()
            elif choice == 4:
                self.balance_enquiry()
            elif choice == 5:
                self.display_account()
            else:
                print("Invalid choice.")



bank = Bank()
bank.menu()
