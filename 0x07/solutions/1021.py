import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
dq = deque(range(1, n + 1))
cnt = 0
targets = list(map(int, input().split()))

for t in targets:
    idx = dq.index(t)
    while (dq[0] != t):
        if (idx <= len(dq) // 2):
            dq.append(dq.popleft())
        else:
            dq.appendleft(dq.pop())
        cnt += 1
    dq.popleft()
print(cnt)