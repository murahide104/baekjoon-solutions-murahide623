n = int(input())
for i in range(n):
    p, t = map(int, input().split())
    die = t//7
    birth = t//4
    print(p-die+birth)