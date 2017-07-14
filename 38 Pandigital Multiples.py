def isPandigital(num):
    for i in range(1,len(str(num))+1):
        if str(i) not in str(num):
            return False
    return True

s = ''
n = 1
maxPandigital = 123456789
for num in range(1,987654):
    while len(s)<9:
        s=s+str(num*n)
        n+=1
    if len(s)==9 and isPandigital(s) and int(s)>maxPandigital:
        maxPandigital = int(s)
    s = ''
    n = 1

print(maxPandigital)
    
