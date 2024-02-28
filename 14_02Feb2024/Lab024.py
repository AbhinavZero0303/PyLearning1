def make_pizza(*topings, base):
    for toping in topings:
        print(toping)
    return topings, base

swathi_a, swathi_b = make_pizza("Tomato", "Mushroom", "sweetcorn", base= "thin")
print(swathi_a)
print(swathi_b)
