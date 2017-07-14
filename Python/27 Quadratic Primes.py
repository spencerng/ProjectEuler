import math
def isPrime(n):
    if n<0:
        return False
    if n%2==0 and not n==0:
        return False
    for i in range(3,int(math.sqrt(n))+1,2):
        if n%i==0:
            return False
    return True

mostPrimes = (0,0,0)
for a in range(-1000,1001):
    for b in range(-1000,1001):
        n = 0
        while isPrime(n**2+a*n+b):
            n+=1
        if n>mostPrimes[2]:
            mostPrimes = (a,b,n)
print(mostPrimes[0]*mostPrimes[1])
