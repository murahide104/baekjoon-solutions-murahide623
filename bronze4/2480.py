L = list(map(int, input().split()))
if L.count(L[0]) == 3:
    print(10000+(L[0]*1000))
elif L.count(L[0]) == 2:
    print(1000+(L[0]*100))
elif L.count(L[1]) == 2:
    print(1000+(L[1]*100))
else:
    print(max(L)*100)