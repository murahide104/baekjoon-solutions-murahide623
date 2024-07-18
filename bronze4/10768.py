a, b = map(int, open(0))
if a == 1:
    print("Before")
elif a == 2 and b < 18:
    print("Before")
elif a == 2 and b > 18:
    print("After")
elif a >= 3:
    print("After")
else:
    print("Special")