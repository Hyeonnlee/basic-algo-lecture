import sys
input = sys.stdin.readline
n, k = map(int, input().split())
l = [i for i in range(1, n + 1)]
ans = []

i = 0
while (len(ans) < n):
    if i % k == k - 1:
        ans.append(l[i])
    else:
        l.append(l[i])
    l += 1
print("<" + ", ".join(map(str, ans)) + ">")