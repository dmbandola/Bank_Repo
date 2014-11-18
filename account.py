class Account(object):
    def __init__(self, account_number, balance):

        self.account_number = account_number
        self.balance = balance

    def check_if_int(self,account_number, balance):
        if type(account_number) != int and type(balance) == int:
            return self.balance
        else:
            raise TypeError("Invalid type: {} and {}".format(type(account_number),type(balance)))


if __name__ == '__main':
    result = Account()
    print result
