import os
os.system('cls')
import time

def cls():
    os.system('cls')

def menu():
    while True:
        try:
            choice = int(input("1)Login 2)Register 3)Quit --> "))
            return choice
        except ValueError:
            print("Please choose a whole number either 1, 2 or 3")

def add():
    global item
    global cost
    item -= 1
    cart.append(items[item])
    cost += int(prices[item])
    return cost


def sizeadd():
    global size
    size -= 1
    chosensize.append(sizes[size])

def remove():
    print("Please state which item you would like to remove.")
    kill = int(input("Enter the number for the item which you would like to remove: "))
    cart.remove(kill)
    cost -=

LoginList = []
chosensize = []
cart = []
minage = 13





#space to seperate and visualize code easier





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
         if age < minage:
             print("no")
             end
         elif age >= minage:
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





#space to seperate and visualize code easier





LoggedIn = True
print("")
print("You are currently logged in to the BDSC uniform shop")
f = open('items.txt', 'r')
items = f.readlines()
f = open('sizes.txt', 'r')
sizes = f.readlines()
f = open('prices.txt', 'r')
prices = f.readlines()
cost = 0

while LoggedIn:
    choice = int(input("1)Shop 2)Edit cart 3)Checkout 4)Logout "))


    if choice == 1:
        print("_____________________________________________")
        print("")
        i = 0
        while i < len(items):
            print("{}. ${} {}".format(i + 1, prices[i], items[i]))
            i += 1
        print("_____________________________________________")
        item = int(input("Please enter the number that corresponds to which item you would like to add to your cart: "))
        add()
        print("_____________________________________________")
        print("")
        i = 0
        while i < len(sizes):
            print("{}. {}".format(i + 1, sizes[i]))
            i += 1
        print("_____________________________________________")
        size = int(input("Please enter the number that corresponds to which size you want the item in: "))
        sizeadd()



    elif choice == 2:
        print("Here is what you currently have in your cart:")
        print("_____________________________________________")
        print("")
        i = 0
        while i < len(cart):
            print("{}. {} {}".format(i + 1, cart[i], chosensize[i]))
            i += 1
        print("_____________________________________________")
        print("Would you like to remove items?")
        confirm = int(input("(1)yes or (2)no: "))
        try:
            if confirm == 1:
                remove()
            elif confirm == 2:
                continue
        except ValueError:
            print("Please enter either 1 or 2 as an integer.")
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
        f.close()
        menu()
