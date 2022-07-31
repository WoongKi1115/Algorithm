a = []
for i in range(9):
    a.append(int(input()))
b = sorted(a)
for i in range(len(a)):
    if b[-1] == a[i]:
        print(b[-1])
        print(i+1)

