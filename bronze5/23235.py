count = 0
while True:
    L = list(map(int, input().split()))
    if L[0] != 0:
        count += 1
        print("Case "+str(count)+": Sorting... done!")
    else:
        break