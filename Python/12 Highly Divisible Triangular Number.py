import math
def numFact(n):
    factors = 0
    if n % math.sqrt(n)==0:
        factors+=1
    for i in range(1,int(math.sqrt(n)-1)):
        if n % i == 0:
            factors+=2
    return factors

    
num = 1
count = 1
while True:
    factors = numFact(num)

    if factors > 500:
        break
    else:
        count+=1
        num+=count
print(num)

    
