s = input().upper()
setList = list(set(s))
best = 0
result = ''
for i in setList:
    if best<s.count(i):
        best = s.count(i)
        result = i
    elif best == s.count(i) and result != i:
        result = '?'
print(result)