N = int(input())
x = 10000000
list1 = [0]
count = 0
for i in range(666,x):
    if '666' in str(i):
        list1.append(i)
        count += 1
        if count == N:
            print(i)
            break
