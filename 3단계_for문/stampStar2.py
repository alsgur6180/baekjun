n = int(input())

for i in range(n-1,-1,-1):#n= 5, 4 3 2 1 0
    for _ in range(i):
        print(' ',end='')
    for _ in range(n-i): 
        print('*', end='')
    print()