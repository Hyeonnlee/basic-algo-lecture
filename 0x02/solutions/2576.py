num = [int(input()) for _ in range(7)]
sum = 0
min_val = 1000
for n in num:
    if (n % 2 != 0):
        sum += n
        if (min_val > n):
            min_val = n
if (sum == 0):
    print(-1)
else:
    print(sum)
    print(min_val)