n = int(input())
for i in range(n):
    L = list(map(int, input().split()))
    if L[0]*L[1] == L[2]*L[3]:
        print("Tie")
    elif L[0]*L[1] >= L[2]*L[3]:
        print("TelecomParisTech")
    else:
        print("Eurecom")