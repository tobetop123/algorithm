a,b,c =map(int,input().split())
if a==b and b==c :
    print(10000+a*1000)
elif a==b or b==c or c==a :
    t =0
    if a==b : t=a
    elif b==c : t=b
    else :
        t=c
    print(1000+t*100)
else :
    l=a
    if l<b :l=b
    if l<c :l=c
    print(l*100)