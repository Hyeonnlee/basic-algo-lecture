import sys

num = [int(sys.stdin.readline()) for _ in range(9)]
result = []
found = False

for a in range(8):
    for b in range(a + 1, 9):
        tmp = []
        total = 0
        for c in range(9):
            if (c != a and c != b):
                tmp.append(num[c])
                total += num[c]
        if total == 100:
            result = tmp
            found = True
            break
    if found:
        break
    
result.sort()
for x in result:
    print(x)