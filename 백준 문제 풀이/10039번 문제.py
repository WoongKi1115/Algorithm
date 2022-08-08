scores = 0
for i in range(5):
    x = int(input())
    if x < 40:
        x = 40
    scores += x
print(scores//5)