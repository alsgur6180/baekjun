n = int(input())
conference =[]
time_range = []
count = 1
for _ in range(n):
    start,end = map(int,input().split())
    time = (end-start)
    conference.append([start,end,time])
conference.sort(key = lambda x:x[2])

for i in range(1,n-1):
    
    if conference[i][0] > conference[i+1][1] or conference[i][1]<conference[i+1][0]:

        
