# 1,2,3을 이용한 네 자릿수를 출력하는 코드 작성
def per(Jary, subset):
    # 종료조건
    if Jary == 4:
        print(*subset)
        return
    # 재귀호출
    for i in range(1,4):
        per(Jary+1, subset + [i])

per(0,[])