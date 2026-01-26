arr = [x for x in range(21)]
for i in range(10):
    A, B = map(int, input().split())
    l, r = A, B
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
for i in range(1, 21):
    print(arr[i], end = " ")