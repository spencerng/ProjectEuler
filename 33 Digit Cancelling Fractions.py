from time import time
t=time()
def gcd(a,b):
    if b==0:
        return a
    return gcd(b, a%b)

num = 1
denom = 1
count = 0
for a in range(10,100):
    for b in range(a,100):     
        for i in range(2):
            for j in range(2):
                if str(a)[i]==str(b)[j]:
                    n1=int(str(a)[1-i])
                    n2=int(str(b)[1-j])
                    
                    if str(b)[j]!='0'  and n2!=0 and a/b < 1 and a/b==n1/n2:                     
                        num*=n1
                        denom*=n2
                        count+=1
                        
print(denom//gcd(num,denom))

print(time()-t)
