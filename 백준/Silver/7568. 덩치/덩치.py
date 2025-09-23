def solution(A):
    B = [1 for _ in range(len(A))]
    
    for i in range(len(A)):
        for j in range(len(A)):
            if A[i][0] < A[j][0] and A[i][1] < A[j][1]:
                B[i] += 1

    for a in B:

        print(a, end=" ")
    
  

a = int(input())
b = []
for _ in range(a):
    c, d = map(int, input().split(' '))
    b.append([c, d])

solution(b)