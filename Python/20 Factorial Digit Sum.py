def fact(n):
    product = 1
    for i in range(1,n+1):
        product*=i
    return product

n = fact(100)
sum = 0
while n !=0:
    sum+=n%10
    n=n//10
print(sum)
