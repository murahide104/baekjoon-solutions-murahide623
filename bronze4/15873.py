n = str(input())
if len(n) == 2:
    print(int(n[0])+int(n[1]))
elif len(n) == 3 and n[1] == "0":
    print(10+int(str(n[2])))
elif len(n) == 3:
    print(int(n[0])+10)
else:
    print(20)