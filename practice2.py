T = int(input())

for tc in range(1, 1+T):
    N = int(input()) # N은 숫자열의 개수
    arr = list(map(int, input().split())) # 숫자열을 리스트로


    for i in range(N-1, 0, -1): # arr의 마지막인덱스부터 두번째 인덱스까지 순회
        for j in range(0, i): # i에는 N-1부터 1까지 들어감. 그러면, 0번~N-2번, 0번~N-3번, ,,, 0번~1번, 0번.
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    print(f"#{tc} ",end="")
    print(*arr)

