a,b,c,d,e = map(int, open(0))
total = 0
if a < 0:
    total += -(a*c)
    total += d
    total += b*e
    print(total)
elif a == 0:
    total += d
    total += b*e
    print(total)
else:
    print((b-a)*e)