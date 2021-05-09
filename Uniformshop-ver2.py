LoginList = []

print("Hi welcome to the BDSC uniform shop")
print("")

def login():

    while True:
        try:
            choice = int(input("1)Login 2)Register 3)Quit --> "))
        except ValueError:
            print("Please choose a whole number either 1, 2 or 3")
            continue

        # login
        if choice == 1:
            Login = input("Enter your login details to continue:")
            if Login in LoginList:
                print ("Success")
                main()
            else:
                print ("Incorrect")
            login()

         # Registration stage
         elif choice ==2:
             if choice ==2:
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
                     Login = input("Enter your master Key:")
                     print("Your master key has been successfully created!")
                     LoginList.append(Login)
                     break

         # Quit option
         elif choice ==3:
             print("Thank you for shopping with us, bye now")
             exit()

         else:
             print("Invalid input, please try again")
