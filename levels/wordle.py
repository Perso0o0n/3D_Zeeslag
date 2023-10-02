import time
import os
from colorama import Fore
import random
import json

class wordle:
    def play_wordle():
        
        print("Aliens have kidnapped you and the only way they will let you go is by playing their game! ")
        time.sleep(0.7)
        print("Type " + "\033[1m" + "info " + "\033[0m" + "for info about the game or " + "\033[1m" + "start " + "\033[0m" + "to start the game.")
        user_input = input("")
        if user_input == "info":        
            print(Fore.RESET + "In this game you will guess the answer by typing several words.")

            time.sleep(3)
            print("For example: The word is 'crane'.")
            time.sleep(1.5)
            print("If you guess the word 'break' it will give the following result: b" + (Fore.LIGHTGREEN_EX + "r" + Fore.YELLOW + "ea" + Fore.RESET + "k")) 
            time.sleep(2)
            print("Green meaning the letter is in the word and in the correct spot. Yellow meaning the letter is in the word but not in the correct spot.")
            time.sleep(2)
            print("You start with 5 lives. Each time you give an incorrect answer you will lose 1 life. Each correct answer gives you an extra life. ")
            time.sleep(2.5)
            print("If you run out of lives, you will lose a " +  "\033[1m" + Fore.YELLOW + "ship" + Fore.RESET + "\033[0m" + ".")
            user_input = "start"
            
        if user_input == "start":

            def pick_random_answer():
                with open("five-letter-words.json", "r") as file:
                    antwoordjson = json.loads(file.read())
                    antwoordlist = antwoordjson["fiveLetterWords"]
                return antwoordlist[random.randint(0, len(antwoordlist) -1)]

            def check_letters(user_input, antwoord):
                # os.system("cls")


                toprint = ""
                for i in range(0, len(user_input)):
                    if user_input[i] == antwoord[i]:
                        toprint += (Fore.LIGHTGREEN_EX + user_input[i] + Fore.RESET)

                    elif user_input[i] in antwoord:
                        toprint += (Fore.YELLOW + user_input[i] + Fore.RESET)
                    else:
                        toprint += user_input[i]
                print(toprint)

            guesses = 0
            antwoord = pick_random_answer()
            user_input = ""

            while user_input != antwoord and guesses < 6:
                user_input = input("Enter a word: ")
                if len(user_input) != len(antwoord):
                    print("Invalid Input, please enter a word with 5 letters. ")
                    time.sleep(0.5)                         
                    continue
                
                check_letters(user_input, antwoord)
                if user_input == antwoord:
                    print("You guessed the word! ")
                    break
                guesses += 1
                if guesses >= 6:
                    print("You are out of lives. Returning to map. ")
                    print("The word was: " + "\033[1m" + antwoord + "\033[0m")
                    return False
            return True