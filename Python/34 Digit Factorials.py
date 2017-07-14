import math
sum = 0
for i in range(10,50001):
    tempSum = 0
    for j in range(len(str(i))):
        tempSum+=math.factorial(int(str(i)[j]))
    if i == tempSum:
        sum+=i
    
print(sum)
