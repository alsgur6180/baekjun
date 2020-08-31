s = input().upper()
best = 0
result = ''
for i in range(len(s)):
    if s.count(s[i])>best:
        best = s.count(s[i])
        result = s[i]
    elif s.count(s[i]) == best and s[i] != result:
        result = '?'
print(result)

//실패