import sys

# Python에서 구현하는 경우 스택 2개 풀이를 사용하는 것을 권장
input = sys.stdin.readline
left = list(input().strip())
right = []

q = int(input())
for _ in range(q):
    cmd = input.split()
    if cmd[0] == 'L':
        if left:
            right.append(left.pop())
    elif cmd[0] == 'D':
        if right:
            left.append(right.pop())
    elif cmd[0] == 'B':
        if left:
            left.pop()
    else:
        left.append(cmd[1])
print(''.join(left + right[::-1]))