import sys

A, K = map(int,sys.stdin.readline().split())
x = list(map(int,sys.stdin.readline().split()))

count = 0
result = -1
for i in range(A-1,0,-1):
    for j in range(0,i):
        if x[j]>x[j+1]:
            x[j],x[j+1]= x[j+1],x[j]
            count += 1
            if count == K:
                result = f"{x[j]} {x[j+1]}"
                
print(result)
    