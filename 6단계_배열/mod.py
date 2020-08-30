numbers = []
for _ in range(10):
    numbers.append(int(input())%42)
numbers = list(set(numbers))
print(len(numbers))