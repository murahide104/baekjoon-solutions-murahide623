L = list(map(int, open(0)))
if sum(L) != 180:
    print("Error")
elif L.count(L[0]) == 2 or L.count(L[1]) == 2:
    print("Isosceles")
elif L.count(60) == 3:
    print("Equilateral")
else:
    print("Scalene")