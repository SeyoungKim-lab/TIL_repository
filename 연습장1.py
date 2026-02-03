#구상
# 덤프횟수(N):834
# arr: 42 68 35 1 70 ... (총100개)
# arr을 만든다.
# 일단 for문을 N번 돈다고 생각하자
# for문 안: arr의 "최댓값에는 1을빼고, 최솟값에는 1을 더한다"

T = 10

for tc in range(1, 1+T):
    N = int(input()) # 덤프횟수
    arr = list(map(int, input().split())) 
    

    # for문을 N번돈다.(=덤프를 N번한다.)
    for k in range(N):
        # max_v : arr의 최댓값
        max_v = 0
        for i in range(100):
            if arr[i] > max_v:
                max_v = arr[i]
                # 맨 마지막에 갱신되는 i는 ..
                maxvalue_index = i

        # min_v : arr의 최솟값
        min_v = 100 
        for j in range(100):
            if arr[j] < min_v:
                min_v = arr[j]
                # 맨 마지막에 갱신되는 j는..
                minvalue_index = j

        #만약 (최대-최소)가 0 또는 1이면 고만해라
        if max_v - min_v <= 1 : 
            break

        arr[maxvalue_index] -= 1
        arr[minvalue_index] += 1

    # 출력하기 전에 최대,최솟값을 한번 더 갱신
    max_v = 0
    for i in range(100):
        if arr[i] > max_v:
            max_v = arr[i]
            
    min_v = 100 
    for j in range(100):
        if arr[j] < min_v:
            min_v = arr[j]

    
            

    print(f"#{tc} {max_v - min_v}")
        

    
        
