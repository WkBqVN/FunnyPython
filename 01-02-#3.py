inputNumber = int(input("Please enter the number:"))
if inputNumber < 3:
    print("Not Correct the number must > 3")
    inputNumber = int(input("Please enter again: "))
res = 0
for i in range(3,inputNumber,3):
    res += i
print(res)
