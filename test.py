import random
a  = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
]
b  = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
]
c = [[0,0,0],[0,0,0],[0,0,0]]
sum = 0
for i in range(3):
    for j in range(3):
        for k in range(3): 
            sum += a[i][k]*b[k][j]
        c[i][j] = sum
print("Matrix a: ",a)
print("Matrix b: ",b)
print("{a} * {b}".format(a=a,b=b))
print("Result: ",c)