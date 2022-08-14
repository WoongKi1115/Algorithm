T = 10

for tc in range(1,T+1):
    num = int(input())
    x = list(map(int, input().split()))
    result = 0 # 조망권 수
    for i in range(2,num-2):  #조망권 확인 위치(좌우 2칸이 기준이므로 0,1, n,n-1은 의미 없음)
        h = 0    # 주변 4개 중 가장 큰 높이 찾기 위함.
        for j in range(i-2,i+3): #주변 4개 중 최대 높이
            if i != j:
                if h < x[j]:
                    h = x[j]
        if x[i]>h:  # 주변 4개보다 높으면 높이 차이만큼 조망권 확보
            result += x[i]-h
    print(f"#{tc} {result}")
