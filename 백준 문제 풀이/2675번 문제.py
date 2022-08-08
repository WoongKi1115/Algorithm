test_num = int(input())
for i in range(test_num):
    repeat, words = map(str, input().split())
    x = ''
    for i in words:
        x = x + i * int(repeat)
    print(x)

