import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
s = []
ans = [-1] * n

for i in range(n - 1, -1, -1):
    while s and s[-1] <= arr[i]:
        s.pop()
    if s:
        ans[i] = s[-1]
    s.append(arr[i])
print(*ans)