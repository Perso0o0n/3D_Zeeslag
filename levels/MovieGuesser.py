import time
import os

class MovieGuesser:

    def StartLevel():
        print("Welcome to guess the movie! In this minigame you will have to guess the movie based on the emoji.")
        time.sleep(3)
        print("Here is an example: " + ('\U0001F981') + (' \U0001F451'))
        time.sleep(5)
        print("Have you thought about it?")
        time.sleep(1.5)
        print("Examples of correct answers: " + "\033[1m" + "Lion King, The Lion King, de Leeuwenkoning." + "\033[0m")
        time.sleep(2)
        
        def check_if_correct(user_input, movie):
            while True:
                user_input = user_input.lower()
                if user_input == movie:
                    print("You are correct! ")
                    break
                else:
                    os.system("cls")
                    user_input = input("Incorrect, try again: " + movie_symbols)


        movie = "fast and furious"
        movie_symbols =  "\U0001F3CE " " \U0001F620"
        user_input = input("What movie is this? " + movie_symbols)
        check_if_correct(user_input, movie)