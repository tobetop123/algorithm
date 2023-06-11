N = int(input())
array =list(map(int,input().split()))
T = 0

for i in range(N):
    T+=array[i]/max(array)*100
print(T/N)

# n = int(input())  # 과목 수
# test_list = list(map(int, input().split()))
# max_score = max(test_list)

# new_list = []
# for score in test_list :
#     new_list.append(score/max_score *100)  # 새로운 점수 생성
# test_avg = sum(new_list)/n
# print(test_avg)