T = int(input())

for tc in range(1, 1+T):
    s = input()

    # s 문자열이 회문인가?
    # 전체를 뒤집어서 원본과 같은지
    # 절반 기준으로 앞과 뒤가 같은지 비교

    N =len(s)

    # 문제에서 원하는 답
    answer = 0 # 회문이 아니다 라고 가정

    for i in range(N//2):
        # 앞쪽 i번 글자와 뒤쪽 N-1-i번 글자를 비교
        # 같으면 다음 글자비교 이어서...
        # 다르면 회문이 아니니까 비교 중단
        if s[i] != s[N-1-i]:
            break
    else:
        # 위의 반복문이 중간에 종료(break)되지 않았다면 실행되는 코드
        # 비교를 하다가 앞과 뒤가 다른 적이 없었다 라는 말이니까 회문 발견
        answer = 1
    print(f"#{tc} {answer}")
