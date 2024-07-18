N, M = map(int, input().split())
A = []
B = []

for i in range(N):
    L = list(map(int, input().split()))
    A.append(L)

for i in range(N):
    L = list(map(int, input().split()))
    B.append(L)

for x in range(len(A)):
    for y in range(len(A[0])):
        A[x][y] += B[x][y]

for i in A:
    print(*i)