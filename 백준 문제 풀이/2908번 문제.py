A, B = map(str,input().split())
x = int(A[::-1])
y = int(B[::-1])
if x > y:
    print(x)
else:
    print(y)