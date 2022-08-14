word = input()
list1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
result = [-1] * 26
for i in range(len(list1)):
    for j in range(len(word)):
        if list1[i] == word[j]:
            if result[i] == -1:
                result[i] = j
            else:
                continue
for i in range(len(result)):
    print(result[i], end = ' ')