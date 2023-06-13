import sys

T = int(sys.stdin.readline())
for _ in range(T):
    S = input()
    print(S[0]+S[len(S)-1])