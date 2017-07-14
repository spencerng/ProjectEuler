def ones(n):
    if n == 1 or n ==2 or n==6:
        return 3
    if n == 3 or n==7 or n==8:
        return 5
    if n==4 or n==5 or n==9:
        return 4
def tens(n):
    if n==2 or n==3 or n==8 or n==9:
        return 6
    if n==4 or n==5 or n==6:
        return 5
    if n==7:
        return 7
totalLetters = 0
for x in range (1,1001):
    i = x
    if i==1000:
       totalLetters+=11 
    else:
        if i>=100:
            totalLetters+=7
            digit = 0
            while i>=100:
                digit+=1
                i-=100
            totalLetters+=ones(digit)
            if i!=0:
                totalLetters+=3
        if i>=20:
            digit = 0
            while i>=10:
                digit+=1
                i-=10
            totalLetters+=tens(digit)
        if i>= 10 and i <20:
            if i==10:
                totalLetters+=3
            if i==11 or i==12:
                totalLetters+=6
            if i==13 or i==14 or i==18 or i==19:
                totalLetters+=8
            if i==15 or i==16:
                totalLetters+=7
            if i==17:
                totalLetters+=9
        elif i!=0:
            totalLetters+=ones(i)
print(totalLetters)
