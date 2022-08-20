T = int(input())
for tc in range(1, T+1):
    problem = input()
    stack = []
    result = 'YES'
    for i in problem:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                result = 'NO'
                break
            stack.pop(-1)
    if len(stack) > 0:
        result = 'NO'
    print(result)