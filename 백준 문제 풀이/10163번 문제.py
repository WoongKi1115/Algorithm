N = int(input())
box = [[0]*1002 for _ in range(1002)]
list1 = [list(map(int,input().split())) for _ in range(N)]
result = []
for i in range(N-1,-1,-1):
    count = 0
    for y in range(list1[i][1],(list1[i][1] + list1[i][3])):
        for x in range(list1[i][0],(list1[i][0]+list1[i][2])):
            if box[y][x] == 0:
                box[y][x] = i+1
                count += 1
    result.append(count)

    count = 0

for i in range(N-1,-1,-1):
    print(result[i])