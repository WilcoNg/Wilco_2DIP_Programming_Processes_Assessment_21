import os
os.system('cls')

def clear():
    system('cls')

LoginList = []
shop = ["nil", "Jumper", "Shirt", "Pantaloons", "Skirt"]
cart = []
sizelist = ["small", "medium", "large"]

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
        main()
    else:
        print ("Incorrect")
    menu()

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

 # Quit option
elif choice == 3:
     print("Thank you for shopping with us, bye now")
     exit()
else:
     print("Invalid input, please try again")


LoggedIn = True
print("You are currently logged in to the BDSC uniform shop")

while LoggedIn:
    choice = int(input("1)Shop 2)Edit cart 3)Checkout 4)Logout "))

    if choice == 1:
        print("Enter the number that coralates to the item and size")
        item = int(input("1. Jumper 2. Shirt 3. Pantaloons 4. Skirt "))
        cart.append(item)
        size = input("1. small 2. medium 3. large ")
        sizelist.append(size)

    elif choice == 2:
        print("Here is what you currently have in your cart:")
        print("_____________________________________________")
        i = 0
        while i <= len(cart):
            show = cart[0+i]
            print(shop[show])
            i = i + 1
        break
        print("s")

    elif choice == 3:
        print("s")

    elif choice == 4:
        LoggedIn = False
        print("Logging out of your session....")
        menu()
