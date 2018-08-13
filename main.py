from sys import exit

import interface

def print_menu():

    print("1.  Make Deposit to Single Account")
    print("2.  Make Payments from Ledger")
    print("3.  Create New Bounty")
    print("0. Exit")

def main():

    while True:

        print("Welcome to the console client for MathPay")
        print_menu()

        try:

            int_input = int(input("Please select from the following menu options:   "))

        except:

            print("Please use numerical entries")

        if(int_input == 0):

            print("Goodbye")
            exit()

        elif(int_input == 1):

            label = input("What is the email for the account you wish to deposit to?   ")

            amount = int(input("How much would you like to deposit?   "))

            interface.deposit(label, amount)

        elif(int_input == 2):

            interface.pay_ledger()

        elif(int_input == 3):

            teaser = input("What is the teaser?   ")

            ptext = input("What is the problem text?   ")

            answer = input("What is the answer?   ")

            instructions = input("What are the additional instructions?   ")

            imgLink = input("What is the image link?   ")

            interface.create_new_bounty(teaser, ptext, answer, instructions, imgLink)

if __name__ == '__main__':
    main()
