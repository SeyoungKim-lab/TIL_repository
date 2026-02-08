T = int(input())

for tc in range(1, T+1):
    # A의 길이 n, B의 길이 m
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 문제에서 원하는 답 => B가 A의 부분수열인가?
    # NO 라고 생각하고 시작
    answer = "NO"

    # A의 인덱스 i, B의 인덱스 j
    # A[0] : B[0] => 1 : 3
    # A[1] : B[0] => 3 : 3 (o)
    # A[2] : B[1] => 2 : 4

    # B의 인덱스 j는 1씩 증가하지 않으니 변수로 따로 관리
    j=0
    # A의 인덱스 i는 아무제한 없이 1씩 증가하니 for문 사용
    for i in range(n):
        # A의 i번 원소와 B의 j번 원소를 비교
        # A의 인덱스 i는 for문이 자동으로 증가시킨다.
        # 같지 않음 => A의 인덱스 i만 증가

        # 같음 => 둘 다 증가
        if A[i] == B[i]:
            j += 1

        # 부분수열이 완성되는 조건
        if j == m:
            # A안에서 B의 원소를 모두 발견했다. => 부분수열
            answer = "YES"
            break

    print(f"#{tc} {answer}")