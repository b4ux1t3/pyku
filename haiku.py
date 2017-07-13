import random
fives = open("five.txt").read().splitlines()
sevens = open("seven.txt").read().splitlines()
def main():
	firstFive = getFirstFive()
	secondFive = getSecondFive(firstFive)
	seven = random.choice(sevens)
	
	output = firstFive + "\n" + seven + "\n" + secondFive
	
	print(output)
	f = open("haiku.txt", "w")
	f.write(output)
	f.close()
	
def getFirstFive():
	firstFive = random.choice(fives)
	if firstFive == "":
		firstFive = getFirstFive()
		return(firstFive)
	else:
		return firstFive
		
def getSecondFive(firstFive):
	secondFive = random.choice(fives)
	if secondFive == firstFive or secondFive == "":
		secondFive = getSecondFive(firstFive)
		return secondFive
	else:
		return secondFive
	
if __name__ == "__main__":
	main()