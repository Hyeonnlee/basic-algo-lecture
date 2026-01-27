s1 = input()
alphabet = [0] * 26
for s in s1:
    alphabet[ord(s) - ord('a')] += 1
for i in range(26):
    print(alphabet[i], end = " ")