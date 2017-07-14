from time import time
t = time()
fibs = [1,1]
count = 2
while len(str(fibs[-1])) < 1000:
    fibs.append(fibs[-1]+fibs[-2])
    count+=1
print(count)
print(time()-t)
