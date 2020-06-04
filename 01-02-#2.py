inputNumber=int(input("Please enter the number you want to make factorial: "))
res = 1;
for i in range(2,inputNumber+1):
    res *= i
print(res)