isPalin = lambda s: str(s)==str(str(s)[::-1])
toBin = lambda num: int(str(bin(num))[2:len(str(bin(num)))])
total = 0
for i in range(1,1000000):
    if isPalin(i) and isPalin(toBin(i)):
        total+=i
    
print(total)
