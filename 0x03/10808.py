s = input()
alphabet = [0] * 26
for c in s:
    if c.isalpha():
        c = c.lower()
        alphabet[ord(c) - ord('a')] += 1

for a in alphabet:
    print(a, end = " ")