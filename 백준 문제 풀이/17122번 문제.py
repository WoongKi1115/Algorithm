T = int(input())

for tc in range(T):
    a, b = map(str,input().split())   # a는 A1 b는 숫자
    x = list(a)               # A1 형태로 들어오기 때문에 A와 1을 나눔.
    box = [[0]*8 for _ in range(8)]    #0으로 채워진 8X8 박스를 만듬.
    value = 1
    box[0][0] = 1
    q = 0     # black이나 white라는 것을 알려주기 위한 변수 설정
    w = 0     # a는 w로 b는 q로 설정
    while value < 64:
        for i in range(8):
            for j in range(8):
                box[i][j] = value    # 박스 각각에 1~64 숫자 대입
                if box[i][j] == int(b):   #박스의 숫자가 b와 같을 때 흰색인지 검은색인지 찾음.
                    if (i + j)%2 != 0:
                        q = 'white'
                    else:
                        q = 'black'
                value += 1

# a는 A C E G 일 때와 B D F H 일 때로 나누어 색을 찾음.
    if x[0] == 'A' or x[0] == 'C' or x[0] == 'E' or x[0] == 'G':
        if int(x[1])%2 != 0:
            w = 'black'
        else:
            w = 'white'
    elif x[0] == 'B' or x[0] == 'D' or x[0] == 'F' or x[0] == 'H':
        if int(x[1]) % 2 != 0:
            w = 'white'
        else:
            w = 'black'
    if w == q:
        print('YES')
    else:
        print('NO')

