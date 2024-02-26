side_1 = float(input("Enter a side"))
side_2 = float(input("Enter a side"))
side_3 = float(input("Enter a side"))
if side_1 == side_2 == side_3:
    print("Equilateral triangle")
elif side_1 == side_2 or side_1 == side_3 and side_2 == side_1 or side_2 == side_3 and side_3 == side_1 or side_3 == side_2:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
