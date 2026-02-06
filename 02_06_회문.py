T = int(input())

for tc in range(1, 1+T):
    # N은 2차원 문자열의 길이
    # M은 우리가 찾아야 하는 회문의 길이
    N, M = map(int, input().split())

    text = [input() for _ in range(N)]

    # 회문문자열 찾기
    answer = ""

    # 모든행, 모든열을 뒤져가며 길이 M짜리 회문을 찾기

    # 가로먼저
    for i in range(N):
        # i행에서 회문을 만들건데 회문의 길이가 M이므로
        # 회문을 만들 수 있는 열 번호가 제한되어 있다.
        # 열번호를 j라고 하면 가능한 j의 범위는 range(N-M+1)
        for j in range(N-M+1):
            # i행 j열에서부터 길이 M짜리 회문을 만들기(확인)
            # M//2 번 비교를 하면 된다.
            for k in range(M//2):
                if text[i][j+k] != text[i][j+M-1-k]:
                    break
            else:
                answer = text[i][j:j+M]
    # 세로 회문 찾기
    for j in range(N):
        for i in range(N-M+1):
            for k in range(M//2):
                if text[i+k][j] != text[i+M-1-k][j]:
                    break
            else:
                for w in range(M):
                    answer += text[i+w][j]

    print(f"#{tc} {answer}")