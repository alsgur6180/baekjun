d = []
result = [1, 3, 5, 7, 9, 20, 31, 42, 53, 64, 75, 86, 97]
for i in range(10,100):
    num = i+(i//10)+(i%10)
    d.append(num)
for i in range(100,1000):
    num = i+(i//100)+(i%10)+(i%100//10)
    d.append(num)
for i in range(1000,9994):
    num = i+(i//1000)+(i%10)+(i%100//10)+(i%1000//100)
    d.append(num)
for i in range(100,9994):
    if i not in d:
        result.append(i)
for i in result:
    print(i)