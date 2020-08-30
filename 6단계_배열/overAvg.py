n = int(input())

test_case =[]
case_avg = []
result = []

for i in range(n):
    case_sum = 0
    test_case.append(list(map(int,input().split(' '))))
    for k in range(1,test_case[i][0]+1):
        case_sum += test_case[i][k]
    case_avg.append(case_sum/test_case[i][0])

for i in range(n):
    case_count =0
    for k in range(1,test_case[i][0]+1):
        if test_case[i][k] > case_avg[i]:
            case_count +=1
    result.append(case_count/test_case[i][0]*100)

for i in result:
    print(f'{i:.3f}%')

