#This program takes a random number between 1 and 10 and asks the user to guess it.


import random


random_num = random.randint(1,10)

print(random_num) # Being used for testing purposes


guess = int(input("What is my number? > "))
small_num = int(input('Lower > '))
large_num = int(input('Higher > '))
replay = input("Would you like to play again? > ")
my_num = "I'm thinking of a number between 1 and 10"


# Here we define the initial greeting to the user that asks them to guess the number
def greeting():
	print(my_num)
	print(guess)
if type(guess) == int:
	user_choice()
else:
	print('Please enter a number')
	greeting()



# Here we have our if statements to compare the user's guess to the value of the random number
def user_choice():
	if guess < random_num:
		print(large_num)
		user_choice() 

	elif guess > random_num:
		print(small_num)
		user_choice()

	elif guess == random_num:
		print "You got it!"
		play_again()
	if type(guess) == int:
		user_choice()
	else:
		print('Please enter a number')
		user_choice()

		


def play_again():
	print(replay)
	if replay == 'yes'.lower():
		greeting()
	else:
		print('Thanks for playing :)')















