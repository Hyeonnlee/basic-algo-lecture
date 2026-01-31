import sys
input = sys.stdin.readline

l = 0
pre = [-1] * 5001
nxt = [-1] * 5001
n, k = map(int, input().split())
v = []

for i in range(1, n + 1):
    pre[i] = n if i == 1 else i - 1
    nxt[i] = 1 if i == n else i + 1
    l += 1

curr = 1
i = 1
while (l != 0):
    if (i == k):
        pre[nxt[curr]] = pre[curr]
        nxt[pre[curr]] = nxt[curr]
        v.append(curr)
        i = 1
        l -= 1
    else:
        i += 1
    curr = nxt[curr]

print("<", end="")
for i in range(len(v)):
    print(v[i], end="")
    if i != len(v) - 1:
        print(",", end=" ")
print(">")