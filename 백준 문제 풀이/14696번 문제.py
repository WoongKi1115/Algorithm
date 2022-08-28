def counting(n,l):
    count = [0]*5
    for i in range(n):
        count[l[i]] += 1
    return count

N = int(input())
for tc in range(N):
    num1, *list1 = map(int,input().split())
    num2, *list2 = map(int, input().split())
    result = 'D'
    for i in range(4,0,-1):
        if counting(num1, list1)[i] > counting(num2,list2)[i]:
            result = 'A'
            break
        elif counting(num1, list1)[i] < counting(num2,list2)[i]:
            result = 'B'
            break
        else:
            continue
    print(result)