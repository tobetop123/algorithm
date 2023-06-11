N,M =map(int,input().split())
array = []
for i in range(N):
    array.append(i+1)

for _ in range(M) :
    i,j =map(int,input().split())
    T =array[i-1]
    array[i-1]=array[j-1]
    array[j-1]=T

for i in range(N):
    print(array[i],end=' ')