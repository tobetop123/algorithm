rows, cols = map(int,input().split())

arr1 = [[0 for _ in range(cols)] for _ in range(rows)]
for j in range(cols):
    test = list(map(int,input().split()))
    for i in range(rows):
        arr1[j][i] = test[i]

arr2 = [[0 for _ in range(cols)] for _ in range(rows)]
for j in range(cols):
    test = list(map(int,input().split()))
    for i in range(rows):
        arr2[j][i] = test[i]

for j in range(cols):
    for i in range(rows):
        print(arr1[j][i] + arr2[j][i] ,end=" ")
    print()

# -----------------------------------------------------------------
# n,m = map(int,input().split())
# a = [list(map(int,input().split())) for _ in range(n)]
# b = [list(map(int,input().split())) for _ in range(n)]

# for i in range(n):
#     for j in range(m):
#         a[i][j] += b[i][j]

# for i in a:
#     print(*i)

# -----------------------------------------------------------------
# A, B = [], []

# N, M = map(int, input().split())

# for row in range(N):
#     row = list(map(int, input().split()))
#     A.append(row)

# for row in range(N):
#     row = list(map(int, input().split()))
#     B.append(row)
    
# for row in range(N):
#     for col in range(M):
#         print(A[row][col] + B[row][col], end=' ')
#     print()