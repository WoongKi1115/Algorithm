test_num = int(input())
test_result = list(map(int,input().split()))
new_result = 0
for i in range(len(test_result)):
    new_result += (test_result[i]/max(test_result))*100

print(new_result/test_num)