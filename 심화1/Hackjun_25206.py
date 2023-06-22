rating = ['A+','A0','B+','B0','C+','C0','D+','D0','F']
grades = [4.5,4.0,3.5,3.0,2.5,2.0,1.5,1.0,0.0]
total  =0
result  =0
test =[]
for _ in range(20):
    list = input().split()
    if list[2] != 'P' :
        total += float(list[1])
        for i in rating:
            if list[2] == i:
                result += grades[rating.index(i)]*float(list[1])
print(round(result/total,6))
# print('%.6f' % (result / total))