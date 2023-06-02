a = int(input()) 
b = int(input())
c = (b%10) * a
d = int((b%100)/10) * a
e = int(b/100) * a
f = a * b
print(c)
print(d)
print(e)
print(f)