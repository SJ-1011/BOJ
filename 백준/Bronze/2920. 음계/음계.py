import sys
input = sys.stdin.readline
A = list(map(int, input().split(' ')))

asc, des = True, True


for i in range(8):
    if A[i] != i + 1:
        asc = False
        break

for i in range(8):
    if A[i] != 8 - i:
        des = False
        break

if asc == True:
    print('ascending')
elif des == True:
    print('descending')
else:
    print('mixed')