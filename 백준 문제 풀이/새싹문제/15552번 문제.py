import sys        #백준 문제 풀 때 반복문에 input을 사용하면 시간초과.
                  #때문에 import sys 이후 input 대신 sys.stdin.readline()을 사용해야함.
testcase = int(input())
a = []
b = []
for i in range(testcase):
    x ,y = map(int,sys.stdin.readline().split())
    a.append(x)
    b.append(y)
    print(a[i]+b[i])