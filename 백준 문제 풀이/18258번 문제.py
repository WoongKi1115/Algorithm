import sys
from collections import deque
N = int(sys.stdin.readline())
queue = deque([])
for tc in range(N):
    problem = sys.stdin.readline().split()
    if problem[0] == 'push':
        queue.append(problem[1])

    elif problem[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif problem[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
    elif problem[0] == 'size':
        print(len(queue))
    elif problem[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif problem[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())

