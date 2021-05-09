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
