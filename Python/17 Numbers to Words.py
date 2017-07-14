def ones2(n):
    if n==0:
        return ""
    if n == 1:
        return "One "
    if n==2:
        return "Two "
    if n==3:
        return "Three "
    if n==4:
        return "Four "
    if n==5:
        return "Five "
    if n==6:
        return "Six"
    if n==7:
        return "Seven"
    if n==8:
        return "Eight"
    if n==9: 
        return "Nine"
def ones(n):
    if n==0:
        return ""
    if n == 1:
        return "One "
    if n==2:
        return "Two "
    if n==3:
        return "Three "
    if n==4:
        return "Four "
    if n==5:
        return "Five "
    if n==6:
        return "Six "
    if n==7:
        return "Seven "
    if n==8:
        return "Eight "
    if n==9: 
        return "Nine "
def tens(n):
    if n<10:
        return ones(n)
    elif n==10:
        return "Ten "
    elif n<20:
        if n==11:
            return "Eleven "
        if n==12:
            return "Twelve "
        if n==13:
            return "Thirteen "
        if n==14:
            return "Fourteen "
        if n==15:
            return "Fifteen "
        if n==18:
            return "Eighteen "
        else:
            return ones2(int(str(n)[1])) + "teen "
    elif n<30:
        return "Twenty " + ones(int(str(n)[1]))
    elif n<40:
        return "Thirty " + ones(int(str(n)[1]))
    elif n<50:
        return "Forty " + ones(int(str(n)[1]))
    elif n<60:
        return "Fifty " + ones(int(str(n)[1]))
    elif n>=80 and n <90:
        return "Eighty " + ones(int(str(n)[1]))
    else:
        return ones2(int(str(n)[0]))+"ty " + ones(int(str(n)[1]))
def hundreds(n):
    if n<100:
        return tens(n)
    if n==0:
        return ""
    
    return str(ones(int(str(n)[0])))+"Hundred "+tens(int(str(n)[2])+10*int(str(n)[1]))
    
def thousands(n):
    if n<1000:
        return hundreds(n)
    if n<10000:
        
        return ones(int(str(n)[0])) + "Thousand " + hundreds(int(str(n)[1])*100+10*int(str(n)[2])+int(str(n)[3]))
    if n<100000:
        return tens(int(str(n)[0:2])) + "Thousand "+ hundreds(int(str(n)[2])*100+10*int(str(n)[3])+int(str(n)[4]))
    
    return str(hundreds(int(str(n)[0:3])))+ "Thousand " + hundreds(int(int(str(n)[3])*100+10*int(str(n)[4])+int(str(n)[5])))
def millions(n):
    if n<1000000:
        return thousands(n)
    if n<10000000:
        return ones(int(str(n)[0]))+"Million "+thousands(int(str(n)[1:7]))
    if n<100000000:
        return tens(int(str(n)[0:2]))+"Million "+thousands(int(str(n)[2:8]))
    return hundreds(int(str(n)[0:3]))+"Million "+thousands(int(str(n)[3:9]))
def billions(n):
    if n < 1000000000:
        return millions(n)
    if n<10000000000:
        return ones(int(str(n)[0]))+"Billion "+millions(int(str(n)[1:10]))
    if n<100000000000:
        return tens(int(str(n)[0:2]))+"Billion "+millions(int(str(n)[2:11]))
    return hundreds(int(str(n)[0:3]))+"Billion "+millions(int(str(n)[3:12]))
def trillions(n):
    if n<1000000000000:
        return billions(n)
    if n<10000000000000:
        return ones(int(str(n)[0]))+"Trillion "+billions(int(str(n)[1:13]))
    if n<100000000000000:
        return tens(int(str(n)[0:2]))+"Trillion "+billions(int(str(n)[2:14]))
    return hundreds(int(str(n)[0:3]))+" Trillion "+billions(int(str(n)[3:15]))
for t in range(int(input())):
    n = int(input())
    if n==0:
        print("Zero")
    else:
        print(trillions(n))
    
                    
