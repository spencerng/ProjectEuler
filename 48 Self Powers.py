import time
t=time.time()
sum = 0
for i in range(1,1001):
    sum+=i**i
print(sum)
print(time.time()-t)
