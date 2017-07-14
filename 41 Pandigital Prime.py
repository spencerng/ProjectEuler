import time
from math import sqrt
t=time.time()
def isPandigital(num):
    for i in range(1,len(str(num))+1):
        if str(i) not in str(num):
            return False
    return True

def isPrime(n):
    if n==2:
        return True
    if n%2==0:
        return False
    for i in range(3,int(sqrt(n)),2):
        if n % i==0:
            return False

    return True


for i in range(3,10000000,2):
    if isPandigital(i) and isPrime(i):
        print(i)
        
print(time.time()-t)
