# question = input("Would you like to play a game?")

# if question == 'YES':
# 	print("Ok let's begin")

# else:
# 	print('????')

import random

random_num = random.randint(1,10)

print(random_num)

print("I'm thinking of a number between 1 and 10")
user_guess = input("What is my number? > ")

if user_guess < random_num:
	print("Please try a larger number")

elif user_guess > random_num:
	("Please try a smaller number")

elif user_guess == random_num:
	print("You got it!")


