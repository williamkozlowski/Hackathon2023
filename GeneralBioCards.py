"""
Author: William Kozlowski
File: GeneralBioCards
Date Completed: March 5rd, 2023
executed in the Main.py file, used if user inputs 'a' into terminal.
"""

import FlashCardBank, random, time

def BioCards(): 
    user_score = 0
    user_skips = 0
    total_num_of_questions = 0

    input("You have choosen the General Biology flash cards\n(please input anything in the terminal to continue):")

    print("____________________________________________\nRules:\n1. Please input the term associated with the defintion into the terminal.\n2. Type 'skip' to skip a question\n3. Type 'exit' to finish the session and show your results\n____________________________________________")

    length_of_bio_list = len(FlashCardBank.BioCards) - 1

    time.sleep(1.5)

    while True:
        random_card = random.randint(0, length_of_bio_list)

        if (random_card % 2) == 0:
            random_card = random.randint(0, length_of_bio_list) #guaranteed the number is odd
        
        else:
            user_answer = input(f"{FlashCardBank.BioCards[random_card]}\n(please input your answer in the terminal): ")

            user_answer = user_answer.lower() # so the answer isn't case sensitive

            if user_answer == FlashCardBank.BioCards[random_card - 1]: #assuming the term answer is 1 minus the definition
                user_score += 1
                total_num_of_questions += 1
            elif user_answer == "skip":
                user_skips += 1
                total_num_of_questions += 1
            elif user_answer == "exit":
                break
            else:
                print("Answer was incorrect.")
                total_num_of_questions += 1

    input(f"____________________________________________\nYour summary:\nNumber of questions correct: {user_score}\nNumber of questions total: {total_num_of_questions}\nNumber of skips: {user_skips}\n(please input anything into the terminal to continue): ")
       


        
    

