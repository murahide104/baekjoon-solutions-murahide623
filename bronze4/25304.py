n = int(input())
total = 0
c = int(input())
for i in range(c):
    a, b = map(int, input().split())
    total += a*b
    
if n == total:
    print("Yes")
else:
    print("No")