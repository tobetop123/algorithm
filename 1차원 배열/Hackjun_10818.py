N = int(input())
V = list(map(int,input().split()))
s = 9999999
l = -1000000
for i in range(len(V)):
    t = V[i]
    if t<s:
        s = t
    if t>l:
        l = t
print(s,l)
# print(min(V),max(V))