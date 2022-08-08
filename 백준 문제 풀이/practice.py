x = [11]
count = 0
for i in x:
    a = list(str(i))
    count += a.count('1')
print(count)