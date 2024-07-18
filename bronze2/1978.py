n = int(input())
L = list(map(int, input().split()))
count = 0
for i in range(n):
    if L[i] == 1:
        continue
    elif L[i] == 2:
        count += 1
        continue
    for j in range(L[i]-2):
        n2 = L[i]/(j+2)
        if n2.is_integer():
            break
    else:
        count += 1

print(count)