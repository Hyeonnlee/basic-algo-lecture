N = int(input())
for i in range(N):
    str1, str2 = map(str, input().split())
    str1, str2 = sorted(str1), sorted(str2)
    
    if (str1 == str2):
        print("Possible")
    else:
        print("Impossible")