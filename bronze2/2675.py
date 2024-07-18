n = int(input())
for i in range(n):
    t = []
    a, b = input().split()
    for i in range(len(b)):
        t.append(b[i]*int(a))
    print(*t, sep="")