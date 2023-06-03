A, B = map(int, input().split())
C = int(input())
c = int(C%60)
C = int(C/60)
if B+c >= 60 : 
    A = A+C+1
    B = B+c-60
else :
    A = A+C
    B = B+c
if A>=24 : A = A-24
print(str(A)+" "+str(B))