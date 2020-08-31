n = input()
count = 99
if int(n)<100:
    print(n)
    exit()
else:
    space = []
    space = set(space)
    for i in range(100,int(n)+1):
        number = str(i)
        for k in range(1,len(number)):
            space.add(int(number[k])-int(number[k-1]))
        if len(space) ==1:
            count +=1
        space.clear()
    print(count)
        