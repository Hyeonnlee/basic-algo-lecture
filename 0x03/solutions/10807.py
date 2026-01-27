N = int(input())
arr = list(map(int, input().split()))
a = [0] * 201
for t in arr:
    a[t + 100] += 1
v = int(input())
print(a[v + 100])