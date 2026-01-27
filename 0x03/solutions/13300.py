import math
N, K = map(int, input().split())
students = [[0] * 2 for _ in range(7)]
for i in range(N):
    gender, grade = map(int, input().split())
    students[grade][gender] += 1
room = 0
for i in range(1, 7):
    for j in range(2):
        room += math.ceil(students[i][j] / K)
print(room)