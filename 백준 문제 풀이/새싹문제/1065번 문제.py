def han(x):
    a = list(str(x))
    if x < 100:
        return x
    elif x<1000:
        if int(a[0])-int(a[1]) == int(a[1])-int(a[2]):
            return x
        else:
            return 'No'
    else:
        return 'No'

    

N = int(input())
count = 0
for i in range(1,N+1):
    if han(i) != 'No':
        count += 1
print(count)
