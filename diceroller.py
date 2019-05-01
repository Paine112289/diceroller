import random
start = 1

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
	num = int(input("How many times shall we roll the dice?"))
	end = int(input("Number of sides on the die you wish to roll?"))
	if end == 6:
		reroll = input("Do you want to reroll 1's and 2's?")
		if reroll == "yes" or reroll == "y":
				start = 3
		print("Rolling the dice...")
		print("The values are....")
		def rand(start, end, num):
			
			res = []
			
			for j in range(num):
				res.append(random.randint(start, end))
			
			return res
		print("Rolling the dice...")
		print("The values are....")
		def rand(start, end, num):
			
			res = []
			
			for j in range(num):
				res.append(random.randint(start, end))
			
			return res
	else:
		print("Rolling the dice...")
		print("The values are....")
		def rand(start, end, num):
			
			res = []
			
			for j in range(num):
				res.append(random.randint(start, end))
			
			return res
	print(rand(start, end, num))
	roll_again = input("Roll the Dice again?")
	if roll_again == "n": print("Thank you for using Chris' dice roller")
