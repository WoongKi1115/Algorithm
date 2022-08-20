N, K = map(int,input().split())
list1 = list(map(int,input().split()))
for i in range(N-1,0,-1):
    for j in range(0, i):
        if list1[j] < list1[j+1]:
            list1[j], list1[j+1] = list1[j+1], list1[j]
print(list1[K-1])