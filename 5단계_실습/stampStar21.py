n = int(input())
if n/2%0.5 == 0:
    odd = int(n/2+0.5)
even = n//2
for i in range(n):
    for _ in range(odd):
        print('* ',end='')
    print()
    for _ in range(even):    
        print(' *',end='')
    print()
