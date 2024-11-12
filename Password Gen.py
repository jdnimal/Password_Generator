import random


while True:
    #Providing various options for type of password.
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters = uppercase_letters.lower()

    letters = uppercase_letters+lowercase_letters
    numbers = "0123456789"
    symbols = "!@#$%^&*()_+-={}:<>?,./\\ "

    all = ""

    #Asking user input for the type of password along with length.
    password_type = input("1.) Only characters \n2.) Characters and numbers \n3.) Characters and symbols \n4.) Characters, numbers and symbols \n\nPlease select type of the password from above options(1, 2, 3 or 4): ")
    password_length = int(input("Please enter length for your password: "))

    #Intializing type of password dependent on user input.
    if password_type == "1":
        all += letters
    elif password_type == "2":
        all = letters + numbers
    elif password_type == "3":
        all = letters + symbols
    elif password_type == "4":
        all = letters + numbers + symbols
    else: print("Invalid Input")

    #Generating the random password and printing it out.
    password = "".join(random.sample(all, password_length))
    print("\nYour randomly generated password is: " + password)

    #Looping if another password is needed.
    loop = (input("Would you like to generate another password(Y/N): ")).lower()
    if loop == "n":
        break
    else: print("\n\n\n")