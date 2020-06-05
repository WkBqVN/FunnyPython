firstNumber = int(input("Please enter the first number: "))
secondNumber = int(input("Please enther the second numer: "))
if firstNumber > secondNumber:
	temp = firstNumber
	firstNumber = secondNumber
	secondNumber = temp
for i in range(firstNumber+1,secondNumber):
    print(i,end=" ")
