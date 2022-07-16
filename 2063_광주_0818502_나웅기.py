N=int(input())
a=list(map(int,input().split()))
b=N//2+1
a.sort()
print(a[b-1])

