class Bank(object):
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account.balance

    def get_account_balance(self, account_number):
        return self.accounts.get(account_number)

    def check_account(self, account):
        if account == account.account_number:
            return account

    def withdraw(self, account_number, balance,  amount):
        if balance > amount:
            withdrawal = balance - amount
            return withdrawal
        else:
            print "Insufficient Amount"
