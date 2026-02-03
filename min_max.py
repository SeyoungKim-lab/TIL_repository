T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_v = arr[0]
    min_v = arr[0]
    # 이 부분에 코드 구현
    print(N, arr)
    print(f'#{tc} {max_v - min_v}')
