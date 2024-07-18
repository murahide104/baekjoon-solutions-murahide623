a, b, c = map(int, input().split())
count = 0
if abs(b - c) == a:
    print(0)
elif abs(b - c) == 0:
    print(a)
else:
    print(a-abs(b-c))
