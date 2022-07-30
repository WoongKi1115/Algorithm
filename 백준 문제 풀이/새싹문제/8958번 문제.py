test_num = int(input())
for i in range(test_num):
    test_case = list(input())
    if test_case[0] == 'O':
        test_case[0] = 1
    else:
        test_case[0] = 0

    for i in range(1,len(test_case)):        
        if test_case[i] == 'O' and type(test_case[i-1]) != int:
            test_case[i] = 1
        elif test_case[i] == 'O' and type(test_case[i-1]) == int:
            test_case[i] = test_case[i-1]+1
        else:
            test_case[i] = 0
    print(sum(test_case))


