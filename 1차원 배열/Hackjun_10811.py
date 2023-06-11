N,M =map(int,input().split())
array =[i+1 for i in range(N)]

for _ in range(M):
    i,j=map(int,input().split())
    temp = array[i-1:j]
    temp.reverse()
    array[i-1:j] = temp

for i in range(N):
    print(array[i], end=' ')