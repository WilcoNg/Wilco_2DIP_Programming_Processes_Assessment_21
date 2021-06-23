#Wilco Ng 12S4 2021 DIP Internal

import os
os.system('cls')
import time
accessing = True #One time use as it allows the while loop to occur.


#Clear function to remove the previous texts and reduce screen cluter.
def cls():
    os.system('cls')


#To implement a name variable and greet the user. It also allows the user to exit
#if they have accidently opened the program.
def start():
    global start
    while True:
        try:
            start = int(input("Hello {}, would you like to start up the program"\
            " (1) yes or (2) no? ".format(name)))
            if start == 1:
                time.sleep(1)
                return
            elif start == 2:
                print("ok bye")
                exit()
            else:
                print("1 or 2 please")
                #Deals with the invalid integers such as "3" or "0".
                continue
        except ValueError:
             print("Please enter in integers either 1, or 2.")


#Allows use to chose their actions in the login stage of the program.
def menu():
    global choice
    while True:
        try:
            choice = int(input("1)Login 2)Register 3)Quit:  "))
            return choice
        except ValueError:
             print("Please enter in integers either 1, 2 or 3.")


#Allows use to quickly pick their account and not have to enter it in, it saves
#time and time is money. It would work kinda of like an autofill.
def loginchoice():
    global login
    while True:
        try:
            login = int(input("Enter the number which corresponds"\
            " to your username/login: "))
            return login
        except ValueError:
             print("Please enter in integers.")


#Takes the value of login and runs it through
#to match the password of that login, it then
#makes the user enter a password
#to match the login's password. Only then it allows the user to enter.
def check(login):
    global accessing
    f = open('passwords.txt', 'r')
    passwordlist = f.readlines()
    realpassword = passwordlist[login].strip()
    #removes the space which allowed the password to be valid and work.
    passwordcheck = input("Enter the password for that username: ").strip()
    if realpassword == passwordcheck:
        accessing = False
        print("")
        print("Success!")
        time.sleep(1)
        f.close()
        return accessing
    elif realpassword != passwordcheck:
        print("")
        print("Incorrect.")
        accessing = True
        time.sleep(1)
        cls()
        return accessing


#Adds an item to the cart and makes sure that
#the cost of that item is considered and included.
def add(item):
    global cost
    item -= 1 #The value is minused by one as lists start from 0.
    cart.append(items[item])
    cost += int(prices[item])
    return cost


#Goes hand in hand with the add function above it
#just adds the size of the item previously chosen.
def sizeadd(size):
    size -= 1 #The value is minused by one as lists start from 0.
    chosensize.append(sizes[size])


#removal function for the edit cart option.
def remove(kill):
    global cost
    kill -= 1 #The value is minused by one as lists start from 0.
    removal = cart[kill]
    removalsize = chosensize[kill]
    index = items.index(removal) #Finding the value of the item in the items'
    #list so that later on we can minus the price of that item.
    cart.remove(removal) #Remove is used instead of kill as the position the
    #items are in might be different to the number they are displayed as.
    chosensize.remove(removalsize)
    cost -= int(prices[index])
    return cost


#Counts up the total amount of similiar items
def tally():
    f = open('items.txt', 'r')
    items = f.readlines()
    i = 0
    while i < len(items):
        amount = cart.count(items[i])
        #counts the amount of occurances of each item in the cart
        print("{} X {}".format(items[i].strip(), amount))
        print("")
        i += 1
    f.close()


#list and preset values.
chosensize = []
cart = []
MINAGE = 12
MAXAGE = 18




#Space to seperate and visualize code easily.



#Start of the program.
print("Hi welcome to the BDSC uniform shop.")
repeater = True #This is so that the repeater loop allows the user to sign out
#and sign into a different user without reseting the program.
#It basically makes it so that the program can start back at this point.
name = input("What is your name? ").strip().capitalize()
start() #Implementation of the name variable and greeting.
while repeater:
    while accessing:
        cls()
        choice = menu()
        if choice == 1: #Login option of the code
            f = open('logins.txt', 'r')
            #Opens external file for usernames/logins.
            loginlist = f.readlines()
            print("_____________________________________________")
            print("")
            i = 0
            while i < len(loginlist):
                print("{}. {}".format(i + 1, loginlist[i]))
                #Displays the usernames/logins nicely.
                i += 1
            print("_____________________________________________")
            loginchoice()
            login -= 1
            checker = loginlist[login]
            print("You have chosen the username: " + checker)
            #Confirmation of chosen username/login.
            f.close()
            accessing = check(login)
            if accessing == False:
                print("loading...") #Was used to test if code was running and
                #reaching this point, kept it in because it looked cool.
                break #Exits loop.
            elif accessing == True:
                continue #Repeats loop.


        #Registration option of the login.
        elif choice == 2:
            while True:
                try:
                     age = float(input("Please enter your age: "))
                except ValueError:
                     print("Please enter in integers.")
                     continue
                if age < MINAGE:
                     print("no, you are too young sorry")
                     #Boots the younglings ( ͡° ͜ʖ ͡°).
                     time.sleep(2)
                     exit()
                elif age >= MINAGE or age <= MAXAGE:
                    #Allows for ages 12-18 to use the code.
                     print("Welcome to the uniform shop app,")
                     print("this login and password will be required the next time you login")
                     print("take note of these as you will be unable to recover it if lost.")
                     print("")
                     print("")
                     f = open('logins.txt', 'a+')
                     #a+ mode allows me to write/append to the file.
                     login = input("Enter your username/login: ").strip()
                     print("Your username/login has been successfully created!")
                     loginlist = f.write('\n') #Write the value to a new line.
                     #Which means that my file can work as a functional list.
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
                     choice = None #Resets choice just in case it keeps the old
                     #choice and runs automatically.
                     break
                continue


        #Exit option of the login.
        elif choice == 3:
             print("Thank you for shopping with us, bye now") #Boots
             exit()
        else:
             print("Invalid input, please try again")
             continue




#Space to seperate and visualize code easily.




    time.sleep(1)
    cls()
    print("You are currently logged in to the BDSC uniform shop")
    f = open('items.txt', 'r') #Opening all the text files so that the code
    #below doesn't get messy and clusters with open functions.
    items = f.readlines()
    f = open('sizes.txt', 'r')
    sizes = f.readlines()
    f = open('prices.txt', 'r')
    prices = f.readlines()
    cost = 0
    #Sets cost to zero so that
    #the previous user's cost will not affect the present user.
    LoggedIn = True



    while LoggedIn:
        while True:
            try:
                choice = int(input("1)Shop 2)Edit/View cart 3)Checkout 4)Logout "))
                #Input for new choice value.
                break
            except ValueError:
                 print("Please enter in integers.")


        #Shop option of the main store code.
        if choice == 1:
            print("_____________________________________________")
            #Seperator lines to make the code easier to view.
            print("")
            i = 0
            while i < len(items):
                print("{}. ${} {}".format(i + 1, prices[i].strip(), items[i]))
                #Strip to remove the random spaces from the text file.
                i += 1
            print("_____________________________________________")
            item = int(input("Please enter the number that corresponds to which "\
            "item you would like to add to your cart: "))
            add(item) #Add item function.
            print("_____________________________________________")
            print("")
            i = 0
            while i < len(sizes):
                print("{}. {}".format(i + 1, sizes[i]))
                i += 1
            print("_____________________________________________")
            size = int(input("Please enter the number that corresponds to which "\
            "size you want the item in: "))
            sizeadd(size) #Add corresponding size of that item.
            time.sleep(1)
            cls()


        #Edit and view cart option of the main store code.
        elif choice == 2:
            print("Here is what you currently have in your cart:")
            print("_____________________________________________")
            print("")
            i = 0
            while i < len(cart):
                print("{}. {} | {}".format(i + 1, cart[i].strip(), chosensize[i]))
                #Displays the number, item and size of that item.
                i += 1
            print("_____________________________________________")
            print("Would you like to remove items?")
            while True:
                try:
                    confirm = int(input("(1)yes or (2)no: "))
                    break
                except ValueError:
                     print("Please enter in integers.")
            if confirm == 1:
                print("Please state which item you would like to remove.")
                kill = int(input("Enter the number for the item which you would "\
                "like to remove: "))
                remove(kill) #Function for removing the selected items.
            elif confirm == 2:
                time.sleep(1)
                cls()
                continue


        #Checkout and pay option of the main store code.
        elif choice == 3:
            print("checkout")
            print("_____________________________________________")
            print("Here's what you have in your cart")
            print("")
            tally()
            #Tally function counts up and displays
            #the number of each item the user has in their cart.
            print("Your total cost is ${}".format(cost))
            print("_____________________________________________")
            pay = int(input("Is this correct (1) yes or (2) no? "))
            if pay == 1:
                id = (input("Please enter your student ID number: "))
                print("Thank you for shopping with us.")
                #Clears cart and sizes for the next user.
                cart.clear()
                chosensize.clear()
            elif pay == 2:
                time.sleep(2)
                cls()
                continue


        #Exit and log out option of the main store code.
        elif choice == 4:
            LoggedIn = False
            #Changes the LoggedIn values to False
            #so that the user has to log back into use the program.
            accessing = True
            #Changes value for accessing to True
            #so that the login while loop and run.
            print("Logging out of your session....")
            #Clears cart and sizes for the next user.
            cart.clear()
            chosensize.clear()
            time.sleep(2)
            f.close()
            cls()
            continue
