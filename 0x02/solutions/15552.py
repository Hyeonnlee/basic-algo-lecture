import sys
# '\n'을 제거하며 입력값을 받았던 input() 함수에서
# '\n'을 포함하여 한 줄을 읽도록 하여 입출력 속도 향상
input = sys.stdin.readline

num = int(input())
for _ in range(num):
    a, b = map(int, input().split())
    print(a + b)