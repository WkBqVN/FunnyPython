inputNumber = int(input("Please enter the number:"))
if inputNumber < 3:
    print("0")
res = 0
for i in range(3,inputNumber,3):
    res += i
print(res)
