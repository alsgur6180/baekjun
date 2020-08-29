n = int(input())*2-1

for i in range(n,0,-2):
    for _ in range((n-i)//2):
        print(' ',end='')
    for _ in range(i):
        print('*',end='')
    print()
for i in range(3,n+1,2):
    for _ in range((n-i)//2):
        print(' ',end='')
    for _ in range(i):
        print('*',end='')
    print()


