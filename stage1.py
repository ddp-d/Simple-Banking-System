# Write your code here
from random import randint

class MyAccount:
    IIN = 400000
    data = {}

    def __init__(self):
        self.card = ""
        self.pin = 0000
        self.customer_ind = None
        self.balance = 0

    def add_account(self):
        self.customer_ind = str(randint(0000000000, 9999999999))
        self.card = str(self.IIN) + self.customer_ind
        self.pin = str(randint(0000, 9999))
        self.data[self.card] = self.pin
        print("Your card has been created")
        return self.card, self.pin

    def print_credentials(self):
        print("Your card number:")
        print(self.card)
        print("Your card PIN:")
        print(self.pin)

    def check_account(self, number, pin):
        if number in self.data.keys():
            if data[number] == pin:
                print("You have successfully logged in!")
                return True
            else:
                return False

    def account_balance(self):
        print("Balance: {}".format(self.balance))




counter = True
data = {}
while counter:
    print("1. Create an account")
    print("2. Log into account")
    print("0. Exit")

    choice = int(input(">"))

    if choice == 0:
        print("Bye!")
        counter = False

    if choice == 1:
        new_account = MyAccount()
        myCard, myPin = new_account.add_account()
        data[myCard] = myPin
        new_account.print_credentials()

    if choice == 2:
        print("Enter your card number:")
        card_num = input()
        print("Enter your PIN:")
        pin_num = input()

        old_account = MyAccount()
        answer = old_account.check_account(card_num, pin_num)
        if answer:
            while answer:
                print("1. Balance")
                print("2. Log Out")
                print("0. Exit")

                new_choice = int(input())
                if new_choice == 0:
                    answer = False
                    counter = False
                    print("Bye!")
                if new_choice == 1:
                    old_account.account_balance()
                if new_choice == 2:
                    print("You have successfully logged out!")
                    answer = False

        else:
            print("Wrong card number or PIN!")
