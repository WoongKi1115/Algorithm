N = int(input())
list1 = [int(input()) for _ in range(N)]
stack = []
num = 0
i = 1
result = []
result1 = []
while result != list1:
    if i > (N+1):
        print("NO")
        result1 = []
        break
    if len(stack) == 0 or stack[-1] != list1[num]:
        stack.append(i)
        result1.append('+')
        i += 1
    else:
        result += [stack.pop(-1)]
        num += 1
        result1.append('-')
for i in range(len(result1)):
    print(result1[i])

