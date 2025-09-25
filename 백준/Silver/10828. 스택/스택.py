import sys
N = int(sys.stdin.readline())
stack = []
for i in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        stack.append(int(command[1]))
    elif command[0] == 'pop':
        if stack == []:
            print(-1)
        else:
            ret = stack.pop()
            print(ret)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if stack == []:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if stack == []:
            print(-1)
        else:
            ret = stack.pop()
            print(ret)
            stack.append(ret)