chul = [list(map(int,input().split())) for _ in range(5)]
sa = [list(map(int,input().split())) for _ in range(5)]
box = [[0] * 5 for _ in range(5)]
def check_bingo(n):
    result = 0
    for i in range(5):
        count = 0
        for j in range(5):
            if n[i][j] == 1:
                count += 1
        if count == 5:
            result += 1
    for j in range(5):
        count = 0
        for i in range(5):
            if n[i][j] == 1:
                count += 1
        if count == 5:
            result += 1
    count_a = 0
    for i in range(5):
        if box[i][i] == 1:
            count_a += 1
        if count_a == 5:
            result += 1
    count_b = 0
    for i in range(5):
        if box[i][4-i] == 1:
            count_b += 1
        if count_b == 5:
            result += 1

    return result

count = 0
for i in range(5):
    flag1 = False
    for j in range(5):
        flag2 = False
        for l in range(5):
            for m in range(5):
                if chul[l][m] == sa[i][j]:
                    box[l][m] = 1
                    count += 1
                    flag2 = True
                    break
            if flag2 == True:
                break
        if check_bingo(box) >= 3:
            flag1 = True
            break
    if flag1 == True:
        break

print(count)

