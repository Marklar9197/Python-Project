# question = input("Would you like to play a game?")

# if question == 'YES':
# 	print("Ok let's begin")

# else:
# 	print('????')

import random


random_num = random.randint(1,10)

print(random_num)

def number_choice():
	print("I'm thinking of a number between 1 and 10")
user_guess = int(input("What is my number? > "))

if user_guess < random_num:
	int(input("Please try a larger number"))

elif user_guess > random_num:
	int(input("Please try a smaller number"))

elif user_guess == random_num:
	print "You got it!"


def replay():
replay = input("Would you like to play again? > ")

if replay == 'yes'.lower():
	number_choice()





