import sys
input = sys.stdin.readline
num = int(input())
stack = []
ans = 0
for _ in range(num):
    h = int(input())
    while stack and stack[-1] <= h:
        stack.pop()
    ans += len(stack)
    stack.append(h)
print(ans)