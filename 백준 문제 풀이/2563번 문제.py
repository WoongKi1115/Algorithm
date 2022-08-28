N = int(input())
box = [[0] * 100 for _ in range(100)]
count = 0
for _ in range(N):
    a, b = map(int,input().split())
    for i in range(b,10+b):
        for j in range(a,10+a):
            if box[i][j] == 0:
                box[i][j] = 1
                count += 1
print(count)


        