import os
os.system('cls')
import time

def cls():
    os.system('cls')

LoginList = []
cart = []
sizelist = []

def menu():
    while True:
        try:
            choice = int(input("1)Login 2)Register 3)Quit --> "))
            return choice
        except ValueError:
            print("Please choose a whole number either 1, 2 or 3")

print("Hi welcome to the BDSC uniform shop")
choice = menu()
# login
if choice == 1:
    Login = input("Enter your login details to continue:")
    if Login in LoginList:
        print ("Success")
        time.sleep(3)
        cls()
    else:
        print ("Incorrect")
    menu()
    cls()

 # Registration stage
elif choice == 2:
     while True:
         try:
             age = float(input("Please enter your age: "))
         except ValueError:
             print("Please enter in integers.")
             continue
         if age < 13:
             print("no")
             end
         elif age >= 13:
             print("Welcome to the uniform shop app,")
             print("this key will be required the next time you login")
             print("take note of this key as you will be unable to recover it if lost.")
             print("")
             print("")
         Login = input("Enter your password:")
         print("Your password has been successfully created!")
         LoginList.append(Login)
         break
         time.sleep(3)
         cls()

 # Quit option
elif choice == 3:
     print("Thank you for shopping with us, bye now")
     exit()
else:
     print("Invalid input, please try again")

LoggedIn = True
print("You are currently logged in to the BDSC uniform shop")
cost = 0

def add():
    global cost
    if item == 1:
        cart.append("Jumper in a:")
        cost = cost + 50
    elif item == 2:
        cart.append("Shirt in a:")
        cost = cost + 30
    elif item == 3:
        cart.append("Pantaloons in a:")
        cost = cost + 40
    elif item == 4:
        cart.append("Skirt in a:")
        cost = cost + 20
    return cost

def sizeadd():
    if size == 1:
        cart.append("small size")
    elif size == 2:
        cart.append("medium size")
    elif size == 3:
        cart.append("large size")
    elif size == 4:
        cart.append("srikar size")

while LoggedIn:
    choice = int(input("1)Shop 2)Edit cart 3)Checkout 4)Logout "))


    if choice == 1:
        item = int(input("1. $50 Jumper 2. $30 Shirt 3. $40 Pantaloons 4. $20 Skirt "))
        add()
        size = int(input("1. small 2. medium 3. large 4. srikar "))
        sizeadd()
        time.sleep(2)
        cls()

    elif choice == 2:
        print("Here is what you currently have in your cart:")
        print("_____________________________________________")
        print("")
        for item in cart:
            print(item)
        print("_____________________________________________")
        time.sleep(5)
        cls()

    elif choice == 3:
        print("checkout")
        print("Your total cost is ${}".format(cost))
        time.sleep(5)
        cls()

    elif choice == 4:
        LoggedIn = False
        print("Logging out of your session....")
        menu()
