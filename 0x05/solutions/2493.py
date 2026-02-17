import sys
input = sys.stdin.readline

N = int(input())
heights = list(map(int, input().split()))
stack = []

for i in range(N):
    while stack and heights[stack[-1]] < heights[i]:
        stack.pop()
    if stack:
        print(stack[-1] + 1, end=" ")
    else:
        print(0, end=" ")

    stack.append(i)