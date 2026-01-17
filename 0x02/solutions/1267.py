num = int(input())
Y = 0
M = 0
nums = list(map(int, input().split()))
for num in nums:
    Y += (int(num / 30) + 1) * 10
    M += (int(num / 60) + 1) * 15

if (Y > M):
    print("M ", M)
elif (Y < M):
    print("Y ", Y)
else:
    print("Y M ", Y)
