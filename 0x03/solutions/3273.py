# 한 줄에 숫자 하나씩 입력되는 경우
# arr = [int(input()) for _ in range(n)]
# 한 줄에 여러 숫자가 입력되는 경우
# arr = list(map(int, input().split()))

n = int(input())
arr = list(map(int, input().split()))
x = int(input())
num = [0] * 2000005
cnt = 0
for a in arr:
    if ((x - a) > 0 and num[x - a] != 0):
        cnt += 1
    num[a] = 1
print(cnt)