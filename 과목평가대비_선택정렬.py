T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    arr = list(map(int, input().split()))
    
    for i in range(N-1): # N-1개만 정렬하겠다.
        min_idx = i # 첫놈을 최솟값으로 가정
        for j in range(i+1, N):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[min_idx] , arr[i] = arr[i], arr[min_idx]
    print(f"#{tc} {arr}")
