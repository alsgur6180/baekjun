n = int(input())
a = n//10
b = n%10
count = 0

while True :
    result = ((a+b)%10)+(b*10)
    a = result//10
    b = result%10
    count += 1
    if result == n:
        break
print(count)
