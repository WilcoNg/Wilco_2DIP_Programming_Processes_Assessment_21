import os
os.system('cls')
import time

def cls():
    os.system('cls')

def menu():
    global choice
    while True:
        try:
            choice = int(input("1)Login 2)Register 3)Quit:  "))
            return choice
            break
        except ValueError:
             print("Please enter in integers either 1, 2 or 3.")
    accessing = True

def check(login):
    login -= 1
    checker = loginlist[login]
    print("You have chosen the username: " + checker)
    f = open('passwords.txt', 'r')
    passwordlist = f.readlines()
    passwordcheck = input("Enter the password for that username: ")
    realpassword = passwordlist[login]
    if realpassword == passwordcheck:
        print("Success!")
        time.sleep(2)
        f.close()
        accessing = False
        next()
    elif realpassword != passwordcheck:
        print("Incorrect.")
        time.sleep(2)
        cls()

def next():
    LoggedIn = True
    time.sleep(1)
    cls()
    print("You are currently logged in to the BDSC uniform shop")
    f = open('items.txt', 'r')
    items = f.readlines()
    f = open('sizes.txt', 'r')
    sizes = f.readlines()
    f = open('prices.txt', 'r')
    prices = f.readlines()
    cost = 0


def add(item):
    global cost
    item -= 1
    cart.append(items[item])
    cost += int(prices[item])
    return cost

def sizeadd(size):
    size -= 1
    chosensize.append(sizes[size])

def remove(kill):
    global cost
    kill -= 1
    removal = cart[kill]
    removalsize = chosensize[kill]
    index = items.index(removal)
    cart.remove(removal)
    chosensize.remove(removalsize)
    cost -= int(prices[index])
    return cost

chosensize = []
cart = []
MINAGE = 13





#space to seperate and visualize code easier





print("Hi welcome to the BDSC uniform shop")
accessing = True

#login
while accessing:

    choice = menu()
    if choice == 1:
        f = open('logins.txt', 'r')
        loginlist = f.readlines()
        print("_____________________________________________")
        print("")
        i = 0
        while i < len(loginlist):
            print("{}. {}".format(i + 1, loginlist[i]))
            i += 1
        print("_____________________________________________")
        login = int(input("Enter the number which corresponds to your username/login: "))
        check(login)

     # Registration stage
    elif choice == 2:
        while True:
            try:
                 age = float(input("Please enter your age: "))
            except ValueError:
                 print("Please enter in integers.")
                 continue
            if age < MINAGE:
                 print("no")
                 exit()
            elif age >= MINAGE:
                 print("Welcome to the uniform shop app,")
                 print("this login and password will be required the next time you login")
                 print("take note of this key as you will be unable to recover it if lost.")
                 print("")
                 print("")
                 f = open('logins.txt', 'a+')
                 login = input("Enter your username/login:")
                 print("Your username/login has been successfully created!")
                 loginlist = f.write('\n')
                 loginlist = f.write(login)
                 f.close()
                 f = open('passwords.txt', 'a+')
                 Password = input("Enter your password:")
                 print("Your password has been successfully created!")
                 passwordlist = f.write('\n')
                 passwordlist = f.write(Password)
                 f.close()
                 time.sleep(3)
                 cls()
                 choice = None
                 break
            continue

     # Quit option
    elif choice == 3:
         print("Thank you for shopping with us, bye now")
         exit()
    else:
         print("Invalid input, please try again")
         continue





#space to seperate and visualize code easier




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
        add(item)
        print("_____________________________________________")
        print("")
        i = 0
        while i < len(sizes):
            print("{}. {}".format(i + 1, sizes[i]))
            i += 1
        print("_____________________________________________")
        size = int(input("Please enter the number that corresponds to which size you want the item in: "))
        sizeadd(size)
        time.sleep(1)
        cls()

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
        if confirm == 1:
            print("Please state which item you would like to remove.")
            kill = int(input("Enter the number for the item which you would like to remove: "))
            remove(kill)
        elif confirm == 2:
            time.sleep(1)
            cls()
            continue
        time.sleep(2)
        cls()

    elif choice == 3:
        print("checkout")
        print("_____________________________________________")
        print("Your total cost is ${}".format(cost))
        print("_____________________________________________")
        pay = input("Is this correct (1) yes or (2) no? ")
        if pay == 1:
            id = input("Please enter your student ID number: ")
            print("K nig")
        elif pay == 2:
            time.sleep(2)
            cls()
            continue

    elif choice == 4:
        LoggedIn = False
        print("Logging out of your session....")
        f.close()
        menu()
