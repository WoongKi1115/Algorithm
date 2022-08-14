# 65~90 대문자, #97~122 소문자
word = input().lower()
result = [0]*123
for i in range(len(word)):
    for j in range(97,123):
        if word[i] == chr(j):
            result[j] += 1
max_num = []
max_count = max(result)
for i in range(97,123):
    if result[i] == max_count:
        max_num.append(i)

if len(max_num) > 1:
    print('?')
elif max_num[0] >96:
    print(chr(max_num[0]-32))

