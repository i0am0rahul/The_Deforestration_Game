import streamlit as st
import time

def choice_1():
    # Choice 1 outcome
    st.write("Good choice! You called the authorities and they were able to stop the illegal logging. However, you soon realize that this is not an isolated incident and deforestation is a big problem in your area.")
    time.sleep(2)

    # Choice 2
    st.write("\nWhat do you do next?")
    choice = st.radio("", ["Join a local environmental group and organize a protest.", "Donate money to a conservation organization."])

    if choice == "Join a local environmental group and organize a protest.":
        # Choice 2 outcome
        st.write("Great job! You organized a successful protest and brought attention to the issue of deforestation in your area. The government has promised to take action to protect the forests.")
        time.sleep(2)

        # Choice 3
        st.write("\nWhat do you do next?")
        choice = st.radio("", ["Volunteer to plant trees in the forest.", "Write a letter to your local newspaper to raise awareness about deforestation.", "Lobby your elected officials to pass laws protecting forests."])

        if choice == "Volunteer to plant trees in the forest.":
            # Choice 3 outcome
            st.write("By volunteering to plant trees, you are helping to restore the forest and prevent further deforestation. You have made a real difference for the environment!")
            time.sleep(2)

            # End of the game
            st.write("\nCongratulations! You have helped stop deforestation in your area and made a difference for the environment.")

        elif choice == "Write a letter to your local newspaper to raise awareness about deforestation.":
            # Choice 3 outcome
            st.write("Your letter raises awareness about deforestation and inspires others to take action. Together, you are able to make a real difference for the environment!")
            time.sleep(2)

            # End of the game
            st.write("\nCongratulations! You have helped stop deforestation in your area and made a difference for the environment.")

        elif choice == "Lobby your elected officials to pass laws protecting forests.":
            # Choice 3 outcome
            st.write("Your lobbying efforts pay off and new laws are passed to protect forests. You have made a real difference for the environment!")
            time.sleep(2)

            # End of the game
            st.write("\nCongratulations! You have helped stop deforestation in your area and made a difference for the environment.")

    elif choice == "Donate money to a conservation organization.":
        # Choice 2 outcome
        st.write("Donating money is a good start, but it's not enough to solve the problem of deforestation. The forests continue to be destroyed and the environment is still at risk.")
        time.sleep(2)

        # End of the game
        st.write("\nGame over. Try again and make different choices to help stop deforestation.")

def main():
    # Introduction
    st.title("Stop Deforestation")
    st.write("Welcome to Stop Deforestation! In this game, you will make choices to help stop deforestation and save the environment.")

    # Start of the game
    st.write("\nYou wake up one morning to find that the forest behind your house is being cut down. What do you do?")
    choice = st.radio("", ["Call the local authorities and report the illegal logging.", "Ignore it and go on with your day."])

    if choice == "Call the local authorities and report the illegal logging.":
        choice_1()

    elif choice == "Ignore it and go on":
        print("Ignore it and go on")

