from posixpath import join
lst = [-1]*26
t = input()

for i in range(len(t)):
    t_index = t.find(t[i])
    num_t = int(ord(t[i])) - 97
    lst[num_t] = t_index

print(*lst)