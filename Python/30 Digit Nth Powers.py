inp = int(input("What power are you checking up to?"))
sumPow = lambda x: sum([int(str(x)[i])**inp for i in range(len(str(x)))])
answer = 0

for i in range(2,1000000):
	if sumPow(i) == i:
		answer+=i
print(answer)
