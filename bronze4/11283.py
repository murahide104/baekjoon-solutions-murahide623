t = input()
enc = str(t.encode('unicode-escape'))
enc = enc[5:9]
print(int(enc,16)-44031)