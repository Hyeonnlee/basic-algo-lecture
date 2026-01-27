ans = 1
for i in range(3):
    ans *= int(input())
num = [0] * 10
while (ans):
    num[ans % 10] += 1
    ans //= 10
for i in range(10):
    print(num[i])