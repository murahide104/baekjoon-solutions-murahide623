L = []
for i in range(9):
    n = int(input())
    L.append(n)
    
print(max(L))
print((L.index(max(L)))+1)