n, d = map(int,input().split())

count = [0]*10
for i in range(1,n+1):
    a = list(str(i))
    for j in range(10):
        count[j] += a.count(str(j))
print(count[d])