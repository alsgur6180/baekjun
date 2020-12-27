count = int(input())
answer = 0

while(1):
    if count%3 ==0:
        count = count/3
    elif (count-1)%3 ==0:
        count = count-1
    elif count%2 ==0:
        count = count/2
    else:
        count = count-1
    answer = answer+1
    if count ==1:
        break
print(answer)

