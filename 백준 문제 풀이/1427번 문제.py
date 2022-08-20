N = list(input())
for i in range(len(N)-1, 0,-1):
    for j in range(0,i):
        if int(N[j]) < int(N[j+1]):
            N[j], N[j+1] = N[j+1], N[j]
result = ''
for i in range(len(N)):
    result += N[i]
print(result)