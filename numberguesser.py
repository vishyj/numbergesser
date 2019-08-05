import random

while True:
	print("Welcome to Number Guesser")
	choice = input("What would you like to do?")
	if choice=="2":
		break
	elif choice == "1":
		minimum = int(input("What is the minimum number?"))
		maximum = int(input("What is the maximum number?"))
	r = random.randint(minimum, maximum)
	while True:
		userChoice = int(input("Guess a number: "))
		if userChoice == r:
			print("Correct")
		elif userChoice < r:
			print("Too Low")
		elif userChoice > r:
			print("Too High")
		else:
			print("Not an option")
