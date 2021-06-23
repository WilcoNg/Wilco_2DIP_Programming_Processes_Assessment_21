import os
os.system('cls')
import time
accessing = True



def cls():
    os.system('cls')



def menu():
    global choice
    while True:
        try:
            choice = int(input("1)Login 2)Register 3)Quit:  "))
            return choice
        except ValueError:
             print("Please enter in integers either 1, 2 or 3.")



def start():
    global start
    while True:
        try:
            start = int(input("Hello {}, would you like to start up the program (1) yes or (2) no? ".format(name)))
            if start == 1:
                return
            elif start == 2:
                print("ok bye")
                exit()
            else:
                print("1 or 2 please")
                continue
        except ValueError:
             print("Please enter in integers either 1, or 2.")



def loginchoice():
    global login
    while True:
        try:
            login = int(input("Enter the number which corresponds to your username/login: "))
            return login
        except ValueError:
             print("Please enter in integers.")



def check(login):
    global accessing
    f = open('passwords.txt', 'r')
    passwordlist = f.readlines()
    realpassword = passwordlist[login].strip()
    passwordcheck = input("Enter the password for that username: ").strip()
    if realpassword == passwordcheck:
        accessing = False
        print("Success!")
        time.sleep(1)
        f.close()
        return accessing
    elif realpassword != passwordcheck:
        print("Incorrect.")
        accessing = True
        time.sleep(1)
        cls()
        return accessing



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



def tally():
    f = open('items.txt', 'r')
    items = f.readlines()
    i = 0
    while i < len(items):
        amount = cart.count(items[i])
        print("{} X {}".format(items[i].strip(), amount))
        print(" ")
        i += 1
    f.close()



chosensize = []
cart = []
MINAGE = 12
MAXAGE = 18









print("Hi welcome to the BDSC uniform shop.")
repeater = True
name = input("What is your name? ").strip().capitalize()
start = start()
while repeater:
    while accessing:
        cls()
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
            loginchoice()
            login -= 1
            checker = loginlist[login]
            print("You have chosen the username: " + checker)
            f.close()
            accessing = check(login)
            if accessing == False:
                print("loading...")
                break
            elif accessing == True:
                continue



        elif choice == 2:
            while True:
                try:
                     age = float(input("Please enter your age: "))
                except ValueError:
                     print("Please enter in integers.")
                     continue
                if age < MINAGE:
                     print("no, you are too young sorry")
                     time.sleep(2)
                     exit()
                elif age >= MINAGE or age <= MAXAGE:
                     print("Welcome to the uniform shop app,")
                     print("this login and password will be required the next time you login")
                     print("take note of this key as you will be unable to recover it if lost.")
                     print("")
                     print("")
                     f = open('logins.txt', 'a+')
                     login = input("Enter your username/login: ").strip()
                     print("Your username/login has been successfully created!")
                     loginlist = f.write('\n')
                     loginlist = f.write(login)
                     f.close()
                     f = open('passwords.txt', 'a+')
                     Password = input("Enter your password: ").strip()
                     print("Your password has been successfully created!")
                     passwordlist = f.write('\n')
                     passwordlist = f.write(Password)
                     f.close()
                     time.sleep(2)
                     cls()
                     choice = None
                     break
                continue



        elif choice == 3:
             print("Thank you for shopping with us, bye now")
             exit()
        else:
             print("Invalid input, please try again")
             continue









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
    LoggedIn = True



    while LoggedIn:
        while True:
            try:
                choice = int(input("1)Shop 2)Edit cart 3)Checkout 4)Logout "))
                break
            except ValueError:
                 print("Please enter in integers.")



        if choice == 1:
            print("_____________________________________________")
            print("")
            i = 0
            while i < len(items):
                print("{}. ${} {}".format(i + 1, prices[i].strip(), items[i]))
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
                print("{}. {} | {}".format(i + 1, cart[i].strip(), chosensize[i]))
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
            print("Here's what you have in your cart")
            print("")
            tally()
            print("Your total cost is ${}".format(cost))
            print("_____________________________________________")
            pay = int(input("Is this correct (1) yes or (2) no? "))
            if pay == 1:
                id = (input("Please enter your student ID number: "))
                print("Thank you for shopping with us.")
            elif pay == 2:
                time.sleep(2)
                cls()
                continue



        elif choice == 4:
            LoggedIn = False
            accessing = True
            print("Logging out of your session....")
            time.sleep(2)
            f.close()
            cls()
            continue
