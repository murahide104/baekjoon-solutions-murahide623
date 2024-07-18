n = str(input())
c2 = 0
total = 0
for i in range(len(n)):
    total += int(n[-(i)-1])*(2**(c2+i))
total *= 17
print(bin(total)[2:])