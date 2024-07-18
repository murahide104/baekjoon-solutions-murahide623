a, b = map(int, input().split()); a *= b
L = list(map(int, input().split()))
for i in range(5):
    L[i] = (L[i]-a)
print(*L)