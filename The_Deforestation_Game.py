import time

# Introduction
print("Welcome to Stop Deforestation! In this game, you will make choices to help stop deforestation and save the environment.")

# Start of the game
print("\nYou wake up one morning to find that the forest behind your house is being cut down. What do you do?")
time.sleep(1)

# Choice 1
print("\n1. Call the local authorities and report the illegal logging.")
print("2. Ignore it and go on with your day.")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    # Choice 1 outcome
    print("\nGood choice! You called the authorities and they were able to stop the illegal logging. However, you soon realize that this is not an isolated incident and deforestation is a big problem in your area.")
    time.sleep(2)

    # Choice 2
    print("\nWhat do you do next?")
    print("1. Join a local environmental group and organize a protest.")
    print("2. Donate money to a conservation organization.")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        # Choice 2 outcome
        print("\nGreat job! You organized a successful protest and brought attention to the issue of deforestation in your area. The government has promised to take action to protect the forests.")
        time.sleep(2)

        # Choice 3
        print("\nWhat do you do next?")
        print("1. Volunteer to plant trees in the forest.")
        print("2. Write a letter to your local newspaper to raise awareness about deforestation.")

        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            # Choice 3 outcome
            print("\nBy volunteering to plant trees, you are helping to restore the forest and prevent further deforestation. You have made a real difference for the environment!")
            time.sleep(2)

            # End of the game
            print("\nCongratulations! You have helped stop deforestation in your area and made a difference for the environment.")

        elif choice == "2":
            # Choice 3 outcome
            print("\nYour letter raises awareness about deforestation and inspires others to take action. Together, you are able to make a real difference for the environment!")
            time.sleep(2)

            # End of the game
            print("\nCongratulations! You have helped stop deforestation in your area and made a difference for the environment.")

        else:
            print("\nInvalid input. Please try again.")

    elif choice == "2":
        # Choice 2 outcome
        print("\nDonating money is a good start, but it's not enough to solve the problem of deforestation. The forests continue to be destroyed and the environment is still at risk.")
        time.sleep(2)

        # End of the game
        print("\nGame over. Try again and make different choices to help stop deforestation.")

    else:
        print("\nInvalid input. Please try again.")

elif choice == "2":
    # Choice 1 outcome
    print("\nIgnoring the problem won't make it go away. The forests continue to be destroyed and the environment is still at risk.")
    time.sleep(2)

    # End of the game
    print("\nGame over. Try again and make different choices to help stop deforestation.")

else:
    print("\nInvalid input. Please try again.")
