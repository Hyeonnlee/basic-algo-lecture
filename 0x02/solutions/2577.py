mul = 1
for i in range(3):
    mul *= int(input())

arr = [0] * 10

for s in str(mul):
    arr[int(s)] += 1

for a in arr:
    print(a)