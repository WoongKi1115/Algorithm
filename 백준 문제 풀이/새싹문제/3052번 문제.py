count = 0
result = []
for i in range(10):
    x = int(input())
    if x%42 in result:
        pass
    else:
        result.append(x%42)
        count += 1
print(count)