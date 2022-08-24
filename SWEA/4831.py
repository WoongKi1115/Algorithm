T = int(input())
for tc in range(1,T+1):
    K, N, M = map(int,input().split())
    a = list(map(int,input().split()))
    station = [0] * (N+1)
    count = 0
    for i in range(M):
        station[a[i]] += 1
    s = 0
    while True:
        k = s
        if s >= N-K:
            break
        a = 0
        for i in range(1,K+1):
            if 0 <= s+i < N:
                if station[s+i] == 1:
                    a = i
            else:
                break
        s += a
        if s == k:
            count = 0
            break
        else:
            count += 1
    print(f"#{tc} {count}")
