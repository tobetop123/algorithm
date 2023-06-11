N=30
M=28
array=[0 for _ in range(N)]

for _ in range(M):
    n=int(input())
    array[n-1] = 1

for i in range(N):
    if array[i] == 0:
        print(i+1)