def high(n):
    count1 = 1
    max_count = 1
    for i in range(N-1):
        if n[i] <= n[i + 1]:
            count1 += 1
            if count1 >= max_count:
                max_count = count1
        else:
            count1 = 1
    return max_count


def low(n):
    count2 = 1
    max_count = 1
    for i in range(N-1):
        if n[i] >= n[i + 1]:
            count2 += 1
            if count2 >= max_count:
                max_count = count2
        else:
            count2 = 1
    return max_count


N = int(input())
list1 = list(map(int, input().split()))
print(max(high(list1),low(list1)))