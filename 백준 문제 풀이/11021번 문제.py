test_case = int(input())
for i in range(1,test_case+1):
    a, b = map(int,input().split())
    c = a + b
    print(f"Case #{i}: {c}")
