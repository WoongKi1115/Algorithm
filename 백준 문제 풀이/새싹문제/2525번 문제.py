H, M = map(int,input().split())
T = int(input())


if (M+T)/60 >= 1:
    if H + (M+T)//60 >= 24:
        H = -24 + (H + (M+T)//60)
        M = (M+T)%60
        print(H, M)
    else:
        H = H + (M+T)//60
        M = (M+T)%60
        print(H, M)
else:
    M = M+T
    print(H, M)