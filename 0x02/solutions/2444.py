num = int(input())
for i in range(num):
    print(' ' * (num - i - 1) + '*' * (2 * i + 1))
for i in range(1, num):
    print(' ' * i + '*' * (2 * (num - i) - 1))