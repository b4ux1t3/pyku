import random
import sys



def main():
	if sys.argv[1] == '-p':
		fives = open("proxy/five.txt").read().splitlines()
		sevens = open("proxy/seven.txt").read().splitlines()
	else:
		fives = open("five.txt").read().splitlines()
		sevens = open("seven.txt").read().splitlines()

	firstFive = getFirstFive(fives)
	secondFive = getSecondFive(fives, firstFive)
	seven = random.choice(sevens)
	
	output = f"{firstFive}\n{seven}\n{secondFive}"
	
	print(output)
	f = open("haiku.txt", "w")
	f.write(output)
	f.close()
	
def getFirstFive(fives):
	firstFive = random.choice(fives)
	if firstFive == "":
		firstFive = getFirstFive()
		return(firstFive)
	else:
		return firstFive
		
def getSecondFive(fives, firstFive):
	secondFive = random.choice(fives)
	if secondFive == firstFive or secondFive == "":
		secondFive = getSecondFive(fives, firstFive)
		return secondFive
	else:
		return secondFive
	
if __name__ == "__main__":
	main()
