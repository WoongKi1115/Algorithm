import sys

testcase = int(input())
a = []
b = []
for i in range(testcase):
    x ,y = map(int,sys.stdin.readline().split())
    a.append(x)
    b.append(y)
    print(a[i]+b[i])