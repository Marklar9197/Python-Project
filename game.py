#This program takes a random number between 1 and 10 and asks the user to guess it.


import random


random_num = random.randint(1,10)

print(random_num) # Being used for testing purposes


guess = int(input("What is my number? > "))
small_num = int(input('Lower > '))
large_num = int(input('Higher > '))
replay = input("Would you like to play again? > ")


def greeting():
	print("I'm thinking of a number between 1 and 10")
	print(guess)
	user_choice()




def user_choice():
if guess < random_num:
		print(large_num)
		user_choice 

elif guess > random_num:
		print(small_num)
		user_choice

elif guess == random_num:
	print "You got it!"
	play_again()



def play_again():
	print(replay)
if replay == 'yes'.lower():
	greeting()













