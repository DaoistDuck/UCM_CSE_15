#Problem 1

name = input("Enter your name here: ")
print("Hello, " + name)

#Problem 2

response = input("Please enter a number: ")
number = int(response)
if(number % 2) == 0:
	print("This number is even")
else:
	print("This number is odd")

#Problem 3

numStr = input("Please enter 10 integers spaced out: ")
numList = numStr.split()
numArray = []
for i in range(0, len(numList)):	
	numArray.append(int(numList[i]))

answer = 0
for i in range(0, len(numList)):
	if(numArray[i] > answer):
		answer = numArray[i]	

print("The Largest integer in this array is ")
print(answer)

#Problem 4

numStr = input("Please enter 10 integers spaced out: ")
numList = numStr.split()
numArray = []
oddNumArray = []
counter = 0
for i in range(0, len(numList)):	
	numArray.append(int(numList[i]))
	if(numArray[i] % 2) == 0:
		counter = counter + 1		
	else:
		oddNumArray.append(numArray[i])

if(counter == 10):
	print("No odd numbers were entered")
else:
	answer = 0
	for i in range(0, len(oddNumArray)):
		if(oddNumArray[i] > answer):
			answer = oddNumArray[i]	
			
	print("The Largest integer in this array is ")
	print(answer)
