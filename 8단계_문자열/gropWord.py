n = int(input())
word = []
count = 0
for _ in range(n):
    word.append(input())
for i in range(n):
    local_count = 0
    for k in range(len(word[i])):
        if word[i].count(word[i][k]) == word[i].rfind(word[i][k])-word[i].find(word[i][k])+1:
            local_count += 1
    if local_count == len(word[i]):
        count +=1
print(count)