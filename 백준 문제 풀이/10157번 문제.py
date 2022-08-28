C, R = map(int,input().split())
num = int(input())
box = [[0]*C for _ in range(R)]
di = [-1,0,1,0]
dj = [0,1,0,-1]
d = 0
ci = R-1
cj = 0
value = 1
Ni = R - 1
Nj = 0
box[ci][cj] = value
result = 1
while value < num:

    Ni = ci + di[d]
    Nj = cj + dj[d]
    for i in range(4):
        d = (d+i)%4
        Ni = ci + di[d]
        Nj = cj + dj[d]

        if 0 <= Ni < R and 0 <= Nj < C and box[Ni][Nj] == 0:
            ci = Ni
            cj = Nj
            break
    else:
        result = 0
    value += 1
    box[Ni][Nj] = value

if result == 0:
    print(0)
else:
    print(Nj + 1, R - Ni)