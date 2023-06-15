T = int(input())
for _ in range(T):
    R,S = map(str,input().split())
    R = int(R)
    S_list = list(S)
    for i in range(len(S_list)):
        for j in range(R):
            print(S_list[i],end='')
    print()

# n = int(input())

# for _ in range(n):
#     cnt, word = input().split()
#     for x in word:
#         print(x*int(cnt), end='')
#     print()