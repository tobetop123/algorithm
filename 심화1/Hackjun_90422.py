arr = [1,1,2,2,2,8]
T = [i for i in map(int,input().split())]

for i in range(len(arr)):
    T[i] = arr[i]-T[i]

for i in range(len(arr)):
    print(T[i],end=' ')