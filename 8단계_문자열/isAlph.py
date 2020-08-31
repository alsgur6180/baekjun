s = input()
result = [-1 for i in range(26)]
for i in range(len(s)):
    for k in range(ord('a'),ord('z')+1):
        if ord(s[i]) == k:
            result[k-ord('a')] = s.find(s[i])
for i in result:
    print(i,end=' ')