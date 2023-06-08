N, X = map(int, input().split())
A = list(map(int,input().split()))
n = ""
for i in range(len(A)):
    T =A[i]
    if T<X:
        n += str(T)+" "
        # print(A[i], end=" ")
print(n)