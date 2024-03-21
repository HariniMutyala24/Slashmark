import random
import time
from os import name as os_name

secret_num = random.randint(1, 200)

def welcome_msg():
    print("May I ask you for your name? : ")
    player = input()
    print(player + ", we are going to play a game. I am thinking of a number between 1 and 200")
    time.sleep(.5)
    print("Go ahead. Guess!")

def make_a_guess():
    num_of_guesses = 0
    while num_of_guesses < 6:
        time.sleep(.25)
        guess_input = input("Guess: ")
        try:
            guessed_num = int(guess_input)

            if 200 >= guessed_num >= 1:
                num_of_guesses += 1
                if num_of_guesses < 6:
                    if guessed_num < secret_num:
                        print("The guess of the number that you have entered is too low")
                    if guessed_num > secret_num:
                        print("The guess of the number that you have entered is too high")
                    if guessed_num != secret_num:
                        time.sleep(.5)
                        print("Try Again!")
                if guessed_num == secret_num:
                    break
            if guessed_num > 200 or guessed_num < 1:
                print("Silly Goose! That number isn't in the range!")
                time.sleep(.25)
                print("Please enter a number between 1 and 200")

        except:
            print("I don't think that " + guess_input + " is a number. Sorry")

    if guessed_num == secret_num:
        num_of_guesses = str(num_of_guesses)
        print('Good job, ' + player + '! You guessed my number in ' + num_of_guesses + ' guesses!')

    if guessed_num != secret_num:
        print('Nope. The number I was thinking of was ' + str(secret_num))

play_more = "yes"
while play_more == "yes" or play_more == "y" or play_more == "Yes":
    welcome_msg()
    make_a_guess()
    print("Do you want to play again? (yes/no or y/n)")
    play_more = input()
