T = int(input())


# 아이디어: 요소의 바로 양옆 2칸이 그 요소보다 작아야함. 그러한 요소의갯수.


for tc in range(1, 1+T):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(2,N-2):
            if arr[i] > arr[i-1] and arr[i] > arr[i-2] and arr[i] > arr[i+1] and arr[i] > arr[i+2]:
                lst = [arr[i-2], arr[i-1], arr[i+1], arr[i+2]]
                max_v = lst[0]
                for j in lst:
                    if j > max_v:
                        max_v = j
                k = arr[i] - max_v
                #합만 갱신하면됨.





