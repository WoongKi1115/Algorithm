a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
ham = [a,b,c]
drink = [d,e]
price = []
for i in range(len(ham)):
    for j in range(len(drink)):
        price.append(ham[i]+drink[j]-50)

result = sorted(price)
print(result[0])