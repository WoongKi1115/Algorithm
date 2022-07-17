def pal(a):
    if a==a[::-1]:
        return(1)
    else:
        return(0)


t=int(input())
for i in range(1,t+1):
    b=input()
    print('#'+str(i)+' '+str(pal(b)))
