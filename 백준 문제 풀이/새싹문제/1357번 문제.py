a, b = map(int, input().split())      # a와 b 값을 정수로 가지고 옴.

def Rev(x):                       #Rev라는 함수를 만듬
    y = str(x)[::-1]              # 문자열로 바꾼 x를 뒤집어줌.
    return int(y)                 # 정수 클래스로 다시 바꾸어줌.
print(Rev(Rev(a)+Rev(b)))


