n = int(input())
if n % 8 == 6:
    print(4)
elif n % 8 == 7:
    print(3)
elif n % 8 == 0:
    print(2)
else:
    print(n%8)
    