from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
outputs = []

q = deque()
for _ in range(n):
    command = list(map(str, input().split()))
    if command[0] == 'push':
        q.append(command[1])
    elif command[0] == 'pop':
        if q:
            output = q.popleft()
        else:
            output = -1
        outputs.append(output)
    elif command[0] == 'size':
        outputs.append(len(q))
    elif command[0] == 'empty':
        if q:
            outputs.append(0)
        else:
            outputs.append(1)
    elif command[0] == 'front':
        if q:
            output = q[0]
        else:
            output = -1
        outputs.append(output)
    elif command[0] == 'back':
        if q:
            output = q[-1]
        else:
            output = -1
        outputs.append(output)

print('\n'.join(map(str, outputs)))