import random

def drawNumber(lower, upper):
	return random.randint(lower,upper)

print("Welcome to the lottery.\nPick the bounds of the lottery:")
lowerLimit = input("Lower limit: ")
upperLimit = input("Upper limit: ")
while upperLimit < lowerLimit:
	print("The upper limit can't be smaller than the lower limit.\n")
	upperLimit = input("Enter the upper limit again: ")
winner = drawNumber(lowerLimit,upperLimit)
pick = 0
while pick!=winner:
	pick = input("Now pick a number: ")
	if pick==winner:
		print("You picked the winning number!\n")
	elif pick < lowerLimit or pick > upperLimit:
		print("Your number is out of range!\n")
	else:
		print("You loose, try again...\n")
