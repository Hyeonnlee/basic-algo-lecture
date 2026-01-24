num = [int(input()) for _ in range(9)]
mx = max(num)
print(mx)
print(num.index(mx) + 1)