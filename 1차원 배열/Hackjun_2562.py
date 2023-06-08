N = 0
number =0
for i in range(9):
    t = int(input())
    if number<t:
        number=t
        N=i+1
print(number)
print(N)
# numbers = [int(input()) for _ in range(9)]

# print(max(numbers))
# print(numbers.index(max(numbers)) + 1)