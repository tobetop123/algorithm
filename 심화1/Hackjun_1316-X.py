N = int(input())
n=N
for _ in range(N):
    S = input()
    for j in range(0, len(S)-1):
        if S[j] == S[j+1]:
            pass
        elif S[j] in S[j+1:]:   #j+1: 이후에 문자열을 비교
            n-=1
            break
print(n)