import sys
input = sys.stdin.readline
n = int(input())

s = []
sum = 0
for _ in range(n):
    x = int(input())
    if x == 0:
        sum -= s[-1]
        s.pop()
    else:
        s.append(x)
        sum += x
print(sum)