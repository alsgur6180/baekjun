number = 1
count = []
for _ in range(3):
    number *= int(input())
numberStr = str(number)
for i in range(10):
    count.append(numberStr.count('%s'%i))
for i in range(10):
    print(count[i])
