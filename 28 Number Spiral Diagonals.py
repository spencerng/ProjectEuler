increment=2
total = 1
num=1
while num < 1001**2:
    for i in range(4):
        num+=increment
        total+=num
    increment+=2
print(total)
