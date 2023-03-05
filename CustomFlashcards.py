"""
Authors: William Kozlowski & Jamin Glass
File: CustomFlashcards.py
Date Completed: March 5rd, 2023
executed in the main file, used when the user types 'd' in the terminal
"""

import random, time

def CustomFlashCards():
    
    user_score = 0
    user_skips = 0
    total_num_of_questions = 0
    num_questions_answered = 0
    custom_flashcard_bank = []

    while True:
        user_input = input("Please input a term, followed by a description of the term, seperated by a comma or type 'exit' to finish the flash cards.\n(Please input answer in terminal): ")
        
        if (user_input == "exit"):
            if custom_flashcard_bank == []: # making sure the user actually inputted something into the test
                print("You didn't input anything into the test! Please try again.")
            else:    
                break

        else:
            index_of_term_split = user_input.find(",") # returns -1 if it cant find a comma

            if (index_of_term_split == -1): 
                print("The term was not seperated by a comma, try again. Please follow the correct format.\n______________________________________")
                continue
            
            else:

                custom_flashcard_bank.append(user_input)
        
        

    input("____________________________________________\nYou have created your custom flash cards.\n(please input anything in the terminal to begin the quiz): ")

    print("____________________________________________\nRules:\n1. Please input the term associated with the defintion into the terminal.\n2. Type 'skip' to skip a question\n3. Type 'exit' to finish the session and show your results\n____________________________________________")

    time.sleep(1.5) # easier on the eyes

    new_card_list = custom_flashcard_bank.copy() # making a copy of the list, so that everytime the test is finished, no data will be lost
    total_num_of_questions = len(new_card_list) # finding total number of questions

    while True:
        
        last_index_of_list = len(new_card_list) - 1 # checking the final index of the list

        random_card_index = random.randint(0, last_index_of_list) # generating a random number between the 0th index and the final index

        random_card = new_card_list.pop(random_card_index) # random card is taken out of the copied list so it doesn't show up again

        index_of_split = random_card.find(",") # finding the index of the split between the term and description

        # spliting term and description into seperate varibles
        random_card_term = random_card[0 : index_of_split] 

        random_card_description = random_card[index_of_split + 1 :]
        
        user_answer = input(f"{random_card_description}\n(please input your answer in the terminal): ") # printing description and asking for term

        user_answer = user_answer.lower() # included so the answer isn't case sensitive

        # going through all possible inputs and how to react
        if user_answer == random_card_term:

            user_score += 1
            num_questions_answered += 1

        elif user_answer == "skip":

            user_skips += 1
            num_questions_answered += 1

        elif user_answer == "exit":

            break

        else:

            print("Answer was incorrect.")
            num_questions_answered += 1
        
        # checking to see if all questions have been answered
        if total_num_of_questions == num_questions_answered:
            break
        else:
            continue

        # doing a final check on performance, to see if the user needs to improve or not
    if (user_score / num_questions_answered) <= 0.5:
        input(f"____________________________________________\nYour summary:\nNumber of questions correct: {user_score}\nNumber of questions total: {num_questions_answered}\nNumber of skips: {user_skips}\n____________________________________________\nYou got more than or exactly 50% of the questions wrong. Consider trying this test again.\n(please input anything into the terminal to continue): ")
    else:
        input(f"____________________________________________\nYour summary:\nNumber of questions correct: {user_score}\nNumber of questions total: {num_questions_answered}\nNumber of skips: {user_skips}\n(please input anything into the terminal to continue): ")