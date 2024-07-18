import math
l,a,b,c,d = map(int, open(0))
a = math.ceil(a/c)
b = math.ceil(b/d)
print(l-max(a,b))