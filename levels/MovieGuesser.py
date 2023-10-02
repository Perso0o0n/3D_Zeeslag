import time
import os

class movie_guesser:
    def play_movie_guesser():
        print("Welcome to guess the movie!")
        time.sleep(1)
        print("Type " + "\033[1m" + "info " + "\033[0m" + "for info about the game or " + "\033[1m" + "start " + "\033[0m" + "to start the game.")
        user_input = input("")
        if user_input == "info":  
            print("In this minigame you will guess the movie based on the emoji.")
            time.sleep(3)
            print("Here is an example: " + ('\U0001F981') + (' \U0001F451'))
            time.sleep(1.5)
            print("Examples of correct answers: " + "\033[1m" + "Lion King, The Lion King, de Leeuwenkoning." + "\033[0m")
            time.sleep(2)
            os.system("cls")
            print("If you struggle with a question you can skip it by typing " + "\033[1m" + "'skip'." + "\033[0m")
            time.sleep(2.5)
            user_input = "start"
        
        if user_input == "start":
            
            def check_if_correct(user_input, movie, hp):
                while True:

                    user_input = user_input.lower()
                    if user_input == movie:
                        os.system("cls")
                        print("You are correct! ")
                        hp += 1
                        break
                    elif user_input == "skip":
                        os.system("cls")
                        print("Skipping question... ")
                        time.sleep(1.5)
                        os.system("cls")
                        break
                    else:
                        if hp > 1:
                            hp = hp - 1 
                            os.system("cls")
                            user_input = input("Incorrect, try again: " + movie_symbols + "\nYou have " + str(hp) + " HP left. ")
                        else:
                            print("You are out of lives, returning to the map.")
                            time.sleep(0.5)
                            return hp
                            #RETURN TO THE MAP
                            
                return hp
                
            hp = 5

            movie = "fast and furious"
            movie_symbols =  "\U0001F3CE  \U0001F620 "
            user_input = input("What movie is this? " + movie_symbols)
            hp = check_if_correct(user_input, movie, hp)


            time.sleep(0.7)

            movie = "frozen"
            movie_symbols = "\U0001F3F0 \U0001F478 \U00002603 "
            user_input = input("What movie is this? " + movie_symbols)
            hp = check_if_correct(user_input, movie, hp)

            time.sleep(0.7)

            movie = "up"
            movie_symbols = "\U0001F474 \U0001F3E0 \U0001F388 "
            user_input = input("What movie is this? " + movie_symbols)
            hp = check_if_correct(user_input, movie, hp)

            time.sleep(0.7)

            movie = "spiderman"
            movie_symbols = "\U0001F577 \U0001F6B6"
            user_input = input("What movie is this? " + movie_symbols)
            user_input = user_input.replace("-", "").replace(" ", "")
            hp = check_if_correct(user_input, movie, hp)

            time.sleep(0.7)

            movie = "titanic"
            movie_symbols = "\U0001F6A2 \U0001F30A \U0001F4A5 "
            user_input = input("What movie is this? " + movie_symbols)
            hp = check_if_correct(user_input, movie, hp)