class Account(object):
    def __init__(self, account_number, balance):

        self.account_number = account_number
        self.balance = balance

    def check_if_int(self, balance):
        if type(balance) == int:
            return self.balance
        else:
            raise TypeError("Invalid type: {}".format(type(balance)))


if __name__ == '__main':
    result = Account()
    print result
