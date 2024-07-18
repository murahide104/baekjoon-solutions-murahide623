t = int(input())
k, b = map(int, input().split())

k = k//2
if k + b <= t:
    print(k+b)
else:
    print(t)