t = int(input())
iter =0
s = ''
result = ''
for _ in range(t):
    iter,s = input().split()
    for j in s:
        for _ in range(int(iter)):
            result += j
    print(result)
    result = ''
    