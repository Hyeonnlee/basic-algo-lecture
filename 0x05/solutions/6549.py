import sys
input = sys.stdin.readline

while True:
    line = input().strip()
    if not line:
        break
    data = list(map(int, line.split()))
    n = data[0]
    if n == 0:
        break
    
    arr = data[1:]
    arr.append(0)

    stack = []
    ans = 0

    for i in range(n + 1):
        while stack and arr[stack[-1]] > arr[i]:
            height = arr[stack[-1]]
            stack.pop()
            if stack:
                width = i - stack[-1] - 1
            else:
                width = i
            ans = max(ans, width * height)
        stack.append(i)

    print(ans)