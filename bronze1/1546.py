n = int(input())
L = list(map(int, input().split()))
total = 0
for i in L:
    total += (i/max(L)*100)

print(total/len(L))