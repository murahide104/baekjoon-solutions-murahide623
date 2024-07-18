t = 0
for i in range(5):
    n = int(input())
    if n < 40:
        t += 40
    else:
        t += n
else:
    print(int(t/5))