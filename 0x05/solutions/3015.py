import sys
input = sys.stdin.readline

stack = []
ans = 0
num = int(input())
for _ in range(num):
    h = int(input())
    cnt = 1
    while stack and stack[-1][0] <= h:
        ans += stack[-1][1]
        if stack[-1][0] == h:
            cnt += stack[-1][1]
        stack.pop()
    if stack:
        ans += 1
    stack.append((h, cnt))
print(ans)
