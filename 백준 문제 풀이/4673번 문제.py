def self_num(x):
    result = x
    for i in (list(str(x))):
        result += int(i)
    return result
a = []
for i in range(1,10001):
    a.append(self_num(i))

for i in range(1,10001):
    if i not in a:
        print(i)

        
