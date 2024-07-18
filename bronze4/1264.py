m = ["a","i","u","e","o","A","I","U","E","O"]
while True:
    t = input()
    count = 0
    if t.count("#") == 1:
        break
    for i in range(10):
        count += t.count(m[i])
    else:
        print(count)