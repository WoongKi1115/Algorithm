N, K = map(int, input().split())
student = [list(map(int, input().split())) for _ in range(N)]

count = [0] * 13

for i in range(N):
    if student[i][0] == 0:
        count[student[i][1]] += 1

    elif student[i][0] == 1:
        count[(student[i][1]) + 6] += 1


result = 0
for i in range(13):
    if count[i] == 0:
        continue
    elif count[i] != 0:
        if count[i] % K == 0:
            result += (count[i] // K)
        else:
            result += (count[i] // K + 1)
print(result)