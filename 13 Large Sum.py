n = 2**1000
print(n)
j = 0
while n!=0:
    j+=(n%10)
    
    n//=10
print(j)
