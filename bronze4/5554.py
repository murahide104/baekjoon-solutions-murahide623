a,b,c,d = map(int, open(0))
a = a+b+c+d
print(a//60); a = a-((a//60)*60)
print(a)