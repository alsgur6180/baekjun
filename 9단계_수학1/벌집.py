import math

n = int(input())

n = math.ceil((n-1)/6)

answer = 0


if n != 0:
    n = n-1
    for i in range(13):
        n = n-i
        answer = i
        if n < 0:
            break

print(answer+1)    

