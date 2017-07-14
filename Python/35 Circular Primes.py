from math import sqrt

def isCircularPrime(n):
    for i in range(len(str(n))):
        if isPrime(n)==False:
            return False
        n = rightRotate(n)
    return True

def rightRotate(n):
    if len(str(n))==1:
        return n
    return int(str(n)[len(str(n))-1]+str(n)[:len(str(n))-1])

def isPrime(n):
    if n%2==0 and not n==2:
        return False
    for i in range(3,int(sqrt(n))+1,2):
        if n%i==0:
            return False

    return True


numPrimes = 1 #account for 2
for i in range(3,1000000,2):
    if isCircularPrime(i):
        numPrimes+=1

print(numPrimes)

