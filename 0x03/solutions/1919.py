s1 = input()
s2 = input()
a1 = [0] * 26
a2 = [0] * 26
cnt = 0
for c in s1:
    a1[ord(c) - ord('a')] += 1
for c in s2:
    a2[ord(c) - ord('a')] += 1
for i in range(26):
    cnt += abs(a1[i] - a2[i])
print(cnt)