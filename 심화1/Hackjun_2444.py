N = int(input())
for i in range(N):
    print(' '*(N-1-i)+'*'+'*'*i*2)
for i in reversed(range(N-1)): # 5 -> 4,3,2,1,0
    print(' '+' '*(N-2-i)+'*'+'*'*i*2)
# for i in range(N,0,-1): # 5 -> 5,4,3,2,1
#     print(' '*(N-i) + '*'*(2*i-1))