test_case = list(map(int,input().split()))
answer = [1, 1, 2, 2, 2, 8]
result = []
for i in range(len(test_case)):
    result.append(answer[i]-test_case[i])
for i in range(len(result)):
    print(result[i], end = ' ')
