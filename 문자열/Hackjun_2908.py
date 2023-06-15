A,B=map(str,input().split()) 
A = int(A[::-1])    #문자열[::-1] : 문자열을 역순정렬
B = int(B[::-1])

if A> B:
    print(A)
else:
    print(B)