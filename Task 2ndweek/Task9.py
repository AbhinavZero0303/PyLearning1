def reverse_string(str):
    reverse = " "
    for c in str:
        reverse = c + reverse
    return reverse



name = reverse_string("Aman")
print(name)
