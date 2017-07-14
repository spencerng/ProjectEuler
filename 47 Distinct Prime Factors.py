def numFact(n):
    count = 2
    facts = []
    while not  n==1:
        if n % count==0:
            n/=count
            if count not in facts:
                facts.append(count)
            count = 2
            continue
        count+=1
    return len(facts)

i = 1
while True:
    if numFact(i)==4 and numFact(i+1)==4 and numFact(i+2)==4 and numFact(i+3)==4:
        break
    i+=1
    print(i)
print(i)
