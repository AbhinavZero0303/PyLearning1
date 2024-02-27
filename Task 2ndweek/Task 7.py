num = int(input("Enter the number\n"))

if num < 0:
    print("Factorial not possible")
elif num == 0:
    print("Factorial-", 1)
else:
    fact = 1
    for i in range(1, num+1):
        fact = fact * i
    print("Factorial is:", fact)
