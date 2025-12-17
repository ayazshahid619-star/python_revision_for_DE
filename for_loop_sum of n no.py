n = int(input("Enter a number: "))

total = 0
for i in range(1, n + 1):
	total = total+i	
	
print("The sum from 1 to", n, "is:", total)

#2nd way

n = int(input("Enter a number: "))

total = n * (n + 1) // 2

print("The sum from 1 to", n, "is:", total)