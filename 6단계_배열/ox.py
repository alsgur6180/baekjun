n = int(input())
ox = []
count = []
score = 0
for _ in range(n):
    count.append(0)
for _ in range(n):
    ox.append(input())
for i in range(n):
    for k in range(len(ox[i])):
        pre = 'O'
        now = ox[i][k]
        if pre == now:
            score += 1
        else:
            score = 0
        if now == 'O':
            count[i] += score
        pre = now
    score = 0
for i in range(n):
    print(count[i])
