import sys #sys모듈 읽어들이기
T = int(sys.stdin.readline())
for _ in range(T):
    A,B = map(int, sys.stdin.readline().split())
    print(A+B)