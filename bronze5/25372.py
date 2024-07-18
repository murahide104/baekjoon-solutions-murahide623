n = int(input())

for i in range(n):
    t = input()
    if (t.index(t[-1],-1)+1) >= 6 and (t.index(t[-1],-1)+1) <= 9:
        print("yes")
    else:
        print("no")