S = input()
n=len(S)
result = 1
if n%2==0:
    for i in range(int(n/2)):
        if S[i]!=S[n-1-i]:
            result=0
else:
    for i in range(int(n/2)-1):
        if S[i]!=S[n-1-i]:
            result=0
print(result)

# word = list(str(input()))

# if list(reversed(word)) == word:
#     print(1)
# else:
#     print(0)