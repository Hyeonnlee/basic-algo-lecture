import sys
input = sys.stdin.readline

num = int(input())
stack = []
cnt = 1
result = []

for _ in range(num):
    x = int(input())

    while cnt <= x:
        stack.append(cnt)
        result.append('+')
        cnt += 1
    if stack and stack[-1] == x:
        stack.pop()
        result.append('-')
    else:
        print("NO")
        sys.exit(0)
print('\n'.join(result))