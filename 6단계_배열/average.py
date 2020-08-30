n = int(input())
sum = 0
numbers = list(map(int,input().split(' ')))
maxNum = max(numbers)

for i in range(n):
    sum += numbers[i]/maxNum*100
print(sum/n)
