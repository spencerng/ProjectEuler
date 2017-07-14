import math
def d(n):
    sum = 1
    for i in range(2,n):
        if n%i==0:
            sum+=i
            
    return sum
sum = 0
for i in range(10000):
    if d(d(i)) == i and i != d(i):
        sum+=i
print(sum)
