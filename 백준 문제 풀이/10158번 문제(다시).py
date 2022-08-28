w, h = map(int,input().split())
p, q = map(int, input().split())
time = int(input())

di = [-1, 1, 1, -1]
dj = [1, 1, -1, -1]
d = 0
# visited = [[0]* (w+1) for _ in range(h+1)]
#
# visited[q][p] = 1
# count = 0
Ni = q
Nj = p
for _ in range(time):
    Ni += di[d]
    Nj += dj[d]
    # visited[Ni][Nj] = 1
    if (Ni == 0 and Nj == 0) or (Ni == 0 and Nj == w) or (Ni == h and Nj == 0) or (Ni == h and Nj == w):
        if d == 1:
            d = 3
        elif d == 0:
            d = 2
        elif d == 2:
            d = 0
        elif d == 3:
            d = 1

    if Nj == w:
        if d == 0:
            d = 3
        elif d == 1:
            d = 2

    elif Ni == 0:
        if d == 3:
            d = 2
        elif d == 0:
            d = 1

    elif Ni == h:
        if d == 2:
            d = 3
        elif d == 1:
            d = 0

    elif Nj == 0:
        if d == 3:
            d = 0
        elif d == 2:
            d = 1

print(Nj, Ni)
    # for i in range(len(visited)):
    #     print(visited[i])

