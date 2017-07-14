import time
t=time.time()
def isPandigital(n):
    for i in range(1,10):
        if str(i) not in str(n) or  len(str(n))!=9:
            return False
    return True

found = []
for i in range(10000):
    for j in range(i,10000):
        if i*j not in found and isPandigital(str(i)+str(j)+str(i*j)):
            found.append(i*j)
            
        
print(sum(found))
print(time.time()-t)
