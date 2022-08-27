N = int(input())
num = list(map(int,input().split()))
student = []
for i in range(N):
    if num[i] == 0:
        student.append(i+1)
    else:
        student.insert(i-num[i],i+1)

for i in range(N):
    print(student[i], end = ' ')