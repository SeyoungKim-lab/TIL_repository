# 3
# 10 3
# 1 2 3 4 5 6 7 8 9 10
# 10 5
# 6262 6004 1801 7660 7919 1280 525 9798 5134 1821 
# 20 19
# 3266 9419 3087 9001 9321 1341 7379 6236 5795 8910 2990 2152 2249 4059 1394 6871 4911 3648 1969 2176


#1 21
#2 11088
#3 1090

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M = map(int,input().split())
    arr = list(map(int, input().split()))
    lst = []
    for i in range(0,N-(M-1)):
        sum_M = 0
        for j in range(i,M+i):
            sum_M = sum_M + arr[j]
        lst.append(sum_M)
    max_v = lst[0]
    min_v = lst[0]
    for i in lst:
        if max_v < i:
            max_v = i
    
    for i in lst:
        if min_v > i:
            min_v = i
    
    print(f'#{test_case} {max_v - min_v}')


    # ///////////////////////////////////////////////////////////////////////////////////
