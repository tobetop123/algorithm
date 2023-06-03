a = int(input())
b = int(input())
x = True
y = True

if a<0 : x =False
if b<0 : y = False
if x==True and y==True: print("1")
elif x==False and y==True : print("2")
elif x==False and y ==False : print("3")
elif x==True and y==False : print("4")
else : print("error")