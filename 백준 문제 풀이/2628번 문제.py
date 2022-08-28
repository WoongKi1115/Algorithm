N, M = map(int,input().split()) # N : 가로 M : 세로
num = int(input())  # 자르는 개수
box = [list(map(int,input().split())) for _ in range(num)]   # 입력된 값

ver = [0, N] # 세로
hor = [0, M] # 가로

for i in range(num):
    if box[i][0] == 1:
        ver.append(box[i][1])
    elif box[i][0] == 0:
        hor.append(box[i][1])

ver.sort()
hor.sort()
ver_count = 0
hor_count = 0
for i in range(len(ver)-1):
    count = ver[i+1] - ver[i]
    if count >= ver_count:
        ver_count = count

for i in range(len(hor)-1):
    count = hor[i+1]- hor[i]
    if count >= hor_count:
        hor_count = count
print(ver_count * hor_count)

