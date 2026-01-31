import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())
Q = deque()

for i in range(1, n + 1):
    Q.append(i)
print("<", end="")

while Q:
    for _ in range(k - 1):
        Q.append(Q.popleft())
    print(Q.popleft(), end="")
    if Q:
        print(", ", end="")
print(">")