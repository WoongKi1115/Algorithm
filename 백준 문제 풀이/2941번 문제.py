word = input()
change = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in change:
    word = word.replace(i, '*')   # 다른 변수로 설정하게 되면 i가 바뀔 때만 적용이 되고 다시 원래의 word로 돌아감.
print(len(word))                         # 때문에 word 자체를 변경시켜주어야함.