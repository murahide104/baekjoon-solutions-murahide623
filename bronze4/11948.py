L = [int(input()) for _ in range(6)]
print(sum(L)-min(L[:4])-min(L[4:]))