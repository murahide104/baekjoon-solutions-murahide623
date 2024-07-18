a, b = map(int, input().split())
check = a/2+b/2
if b == 0:
    print(a, 0)
elif a < b:
    print(-1)
elif check.is_integer():
    print(int(a/2+b/2),int(a/2-b/2))
else:
    print(-1)