w = int(input("Weights: "))
uint = input("L or kg")
if (uint.upper() == 'L'):
    c = uint * .45
    print(f"You are {c} kilos")
else:
    c = uint / .45
    print(f"You are {c} punds")
