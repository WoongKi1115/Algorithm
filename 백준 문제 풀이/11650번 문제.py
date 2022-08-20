# 버블정렬 사용하면 답은 나오지만 시간초과가 뜬다..
#
# import sys
# T = int(sys.stdin.readline())
# box = [list((map(int, sys.stdin.readline().split()))) for _ in range(T)]
# for i in range(T-1, 0, -1):
#     for j in range(i):
#         if box[j][0] > box[j+1][0]:
#             box[j],box[j+1] = box[j+1], box[j]
#         elif box[j][0] == box[j+1][0]:
#             if box[j][1] > box[j+1][1]:
#                 box[j], box[j + 1] = box[j + 1], box[j]
# for i in range(T):
#     a = box[i][0]
#     b = box[i][1]
#     print(a, b)
T = int(input())
box = [list((map(int, input().split()))) for _ in range(T)]
box.sort()
for i in range(T):
    print(box[i][0], box[i][1])