S = input()
S_list = list(S)

for i in range(len(S_list)):
    if S_list[i] =='A'or S_list[i] =='B'or S_list[i] =='C':
        S_list[i] = 2
    elif S_list[i] =='D'or S_list[i] =='E'or S_list[i] =='F':
        S_list[i] = 3
    elif S_list[i] =='G'or S_list[i] =='H'or S_list[i] =='I':
        S_list[i] = 4
    elif S_list[i] =='J'or S_list[i] =='K'or S_list[i] =='L':
        S_list[i] = 5
    elif S_list[i] =='N'or S_list[i] =='M'or S_list[i] =='O':
        S_list[i] = 6
    elif S_list[i] =='P'or S_list[i] =='Q'or S_list[i] =='R'or S_list[i] =='S':
        S_list[i] = 7
    elif S_list[i] =='T'or S_list[i] =='U'or S_list[i] =='V':
        S_list[i] = 8
    elif S_list[i] =='W'or S_list[i] =='X'or S_list[i] =='Y'or S_list[i] =='Z':
        S_list[i] = 9

print(sum(S_list)+len(S_list))

# alpabet_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
# word = input()

# time = 0
# for unit in alpabet_list :  
#     for i in unit:  # alpabet 리스트에서 각 요소를 꺼내서 한글자씩 분리
#         for x in word :  # 입력받은 문자를 하나씩 분리
#             if i == x :  # 두 알파벳이 같으면
#                 time += alpabet_list.index(unit) +3  # time = time + index +3
# print(time)
