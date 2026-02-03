T = int(input())
# 테스트케이스 개수

for tc in range(1, T+1):
    # 테스트 케이스 수만큼 반복, 출력형식 맞추기 위해서 1부터

    N = int(input())
    # 리스트길이 N
    arr = list(map(int, input().split()))
    # N개의 숫자

    # 문제에서 원하는 답(최대값)
    # 일단 맨 앞에있는 원소가 가장크다고 가정
    max_value = arr[0]

    # 반복문을 돌면서 더 큰값을 발견하면 갱신
    for i in range(1,N):
        if arr[i] > max_value:
            max_value = arr[i]

    # 반복문이 끝나면 최대값이 구해진다.
    # 문제에서 원하는 출력형식에 맞게 답 출력
    print(f"#{tc} {max_value}")

3
5
100 9 50 20 10
1
99
3
1 2 3
