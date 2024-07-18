for i in range(3):
    total = 0
    start = 0
    end = 0
    h = 0
    m = 0
    h1,m1,s1,h2,m2,s2 = map(int, input().split())
    start += (h1*60*60)+(m1*60)+s1
    end += (h2*60*60)+(m2*60)+s2
    total = end - start
    h = total // 3600 ; total -= h*3600
    m = total // 60 ; total -= m*60
    print(h,m,total)