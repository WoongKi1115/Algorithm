rt = [list(map(int,input().split())) for _ in range(4)]
box = [[0]*100 for _ in range(100)]
count = 0
for i in range(4):
    for x in range(rt[i][0], rt[i][2]):
        for y in range(rt[i][1], rt[i][3]):
            if box[y][x] == 0:
                box[y][x] += 1
                count += 1

print(count)

