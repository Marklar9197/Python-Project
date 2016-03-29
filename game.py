#This program takes a random number between 1 and 10 and asks the user to guess it.


import random


random_num = random.randint(1,10)

print(random_num) # Being used for testing purposes


guess = int(input("What is my number? > "))

def greeting():
	print("I'm thinking of a number between 1 and 10")
	print(guess)
	user_choice()




def user_choice():
	if guess < random_num:
		large_num = int(input("Please try a larger number > "))
		user_choice 

elif guess > random_num:
		small_num= int(input("Please try a smaller number > "))
		user_choice

elif guess == random_num:
	print "You got it!"
	play_again()



def play_again():
	replay = input("Would you like to play again? > ")
if replay == 'yes'.lower():
	greeting()













