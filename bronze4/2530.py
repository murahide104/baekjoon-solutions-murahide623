time_h = 0
time_m = 0
time_s = 0

time = list(map(int, input().split()))
s = int(input())
time_s += (time[0]*60*60); time_s += (time[1]*60); time_s += time[2]
time_s += s
time_h += time_s//(60**2); time_s -= (time_s//(60**2))*(60**2)
time_m += time_s//60; time_s -= (time_s//60)*60
print(time_h%24, time_m, time_s)