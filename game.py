#This program takes a random number between 1 and 10 and asks the user to guess it.


import random


random_num = random.randint(1,10)

print(random_num) # Being used for testing purposes


def greeting():
	print("I'm thinking of a number between 1 and 10")
user_guess = int(input("What is my number? > "))



def user_choice():
	if user_guess < random_num:
	int(input("Please try a larger number > "))
	return 

elif user_guess > random_num:
	int(input("Please try a smaller number > "))

elif user_guess == random_num:
	print "You got it!"
	replay()



def replay():
	replay = input("Would you like to play again? > ")

if replay == 'yes'.lower():
	number_choice()













