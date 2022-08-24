while True:
    problem = input()
    stack = []
    result = 'yes'
    if problem == '.':
        break

    for i in range(len(problem)):
        if problem[i] == '.':
            break
        if problem[i] == '(' or problem[i] == '[':
            stack.append(problem[i])
        if problem[i] == ')' or problem[i] == ']':
            if len(stack) == 0:
                result = 'no'
                break
            x = stack.pop()
            if not ((x == '(' and problem[i] == ')') or (x == '[' and problem[i] == ']')):
                result = 'no'
                break
    if len(stack) != 0:
        result = 'no'
    print(result)