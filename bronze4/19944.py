a, b = map(int, input().split())
if a >= b:
    if 2 < b:
        print("OLDBIE!")
    else:
        print("NEWBIE!")
else:
    print("TLE!")