h1, b1 = map(int, input().split())
h2, b2 = map(int, input().split())
h1 = h1*3+b1; h2 = h2*3+b2
if h1 > h2:
    print(1,h1-h2)
elif h1 < h2:
    print(2,h2-h1)
else:
    print("NO SCORE")