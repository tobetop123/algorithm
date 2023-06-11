N=10
M=42
array=[0 for _ in range(42)]
T=0

for _ in range(10):
    n=int(input())
    n=n%M
    if array[n-1]==0 :
        array[n-1] =1

for i in range(M):
    if array[i] ==1:
        T+=1
print(T)