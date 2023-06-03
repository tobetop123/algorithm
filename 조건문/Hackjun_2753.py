a = int(input())
result = False
if (a%4) ==0 :
    if (a%100) != 0 or (a%400) ==0:
        result=True

if result :
    print("1")
else :
    print("0")