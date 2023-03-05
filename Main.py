"""
Authors: William Kozlowski & Jamin Glass
File: Main.py
Date Completed: March 5rd, 2023
main excution of the flashcard program
"""

import time, GeneralBioCards, GeneralChemCards, GeneralPhysicsCards, CustomFlashcards

print ("        Flash Card Generator        \nby: William Kozlowski and Jamin Glass")

time.sleep(1.5)

while True:

    user_choice = input("______________________________________\nPlease input an option below:\na. General Biology\nb. General Chemistry\nc. General Phyiscs\nd. Custom Flash Cards\n(please print either 'a', 'b', 'c', or 'd' in terminal, or print 'exit' to exit the session): ")

    if user_choice == "a":
        print("______________________________________") #easier on the eyes
        GeneralBioCards.BioCards()

    elif user_choice == "b":
        print("______________________________________") #easier on the eyes
        GeneralChemCards.ChemCards()

    elif user_choice == "c":
        print("______________________________________") #easier on the eyes
        GeneralPhysicsCards.PhysicsCards()

    elif user_choice == "d":
        print("______________________________________") #easier on the eyes
        CustomFlashcards.CustomFlashCards()

    elif user_choice == "exit":
        print("______________________________________\nUntil next time!")
        break    
        
    else:
        print("Incorrect input, try again.")

    