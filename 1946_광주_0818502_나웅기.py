T=int(input())
for i in range(1,T+1):
    n=int(input())
    b=''
    for a in range(0,n):
        ci, ki = input().split()
        b+=ci*int(ki)
    print('#'+str(i))
    for c in range(1,len(b)+1,10):
        print(b[c-1:c+10-1])
