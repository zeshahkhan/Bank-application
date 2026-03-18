import bankcore
import accounts




def banking_menu(customer_id):
  
    while True:
        print("\n --Bankking Menu--")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Logout")

        choice = input("Enter choice:")

        if choice == "1":
            balance = accounts.check_balance(customer_id)
            print("your balance is:",balance)

        elif choice == "2":
            amount = int(input("Enter amount:"))
            accounts.deposit(customer_id, amount)

        elif choice == "3":
            amount = int(input("Enter amount:"))
            accounts.withdraw(customer_id, amount)

        elif choice == "4":
            print("Logged out")

            break

        else:
            print("Invalid choice")
def main():

    print("Welcome to ABC Bank")

    while True:

        print("\n1. Create an account")
        print("2. Login to the account")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":

            name = input("Enter name: ")
            password = input("Enter password: ")

            bankcore.create_account(name, password)

        elif choice == "2":

            cid = input("Enter Customer ID: ")
            password = input("Enter Password: ")

            if bankcore.login(cid, password):
                banking_menu(cid)

        elif choice == "3":
            print("Thank you for using ABC Bank")
            break

        else:
            print("Invalid option")


main()
