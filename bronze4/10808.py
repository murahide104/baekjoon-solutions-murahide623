a = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
     "n","o","p","q","r","s","t","u","v","w","x","y","z"]
c = [0]*26
t = input()
for i in range(len(t)):
    c[a.index(t[i])] += 1
print(*c)