n = int(input("Enter the Number:"))
count = 0
for i in range(1, n + 1):
    if (n % 1 == 0) and (n % i == 0):
        print("Prime Number", i)
        count = count + 1
if(count == 2):
    print("Its a Prime Number")
else:
    print("Its Not a Prime Number")
