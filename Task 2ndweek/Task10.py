def fact(num):
    f = 1
    for i in range(1, num + 1):
        f = f * i
    return f


number = int(input("Enter a number"))
result = fact(number)
print(result)
