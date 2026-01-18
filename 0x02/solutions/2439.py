num = int(input())
for i in range(num):
    print(' ' * (num - i - 1) + '*' * (i + 1))
    # print(' ' * (num - i - 1), '*' * (i + 1))
    # 구분자(,)는 공백을 포함함 