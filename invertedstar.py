a = int(input("Enter the number of rows: "))
for i in range(a):
    for i in range(a - i):
        print("*", end=" ")
    print()