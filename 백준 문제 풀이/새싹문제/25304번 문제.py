
X = int(input())
N = int(input())
cash = 0
for i in range(N):
    a, b = map(int,input().split())
    cash += a*b
if cash == X:
    print('Yes')
else:
    print('No')
