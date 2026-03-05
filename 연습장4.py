
T =int(input())

for tc in range(1,1+T):
    # N: square의 세로길이
    # M: square의 가로길이
    N, M = map(int, input().split())
    square = [input() for _ in range(N)]
    code = ""
    code_table = {
    "0001101": "0",
    "0011001": "1",
    "0010011": "2",
    "0111101": "3",
    "0100011": "4",
    "0110001": "5",
    "0101111": "6",
    "0111011": "7",
    "0110111": "8",
    "0001011": "9",
    }
    def find_code():
        global code
        odd_sum = 0
        even_sum = 0
        answer = 0
        for i in range(N):
            for j in range(M-1,50, -1):
                if square[i][j] == "1":
                    # 코드 의심 부분
                    line = square[i][j - 55:j + 1]
                    
                    for k in range(0,56,7):    # k는 7개코드의 첫숫자
                        code += code_table[line[k:k+7]]
                    # 코드 검증 (code의 홀수자리합*3 + 짝수자리합 = 10의배수)
                    for w in range(4):
                        even_sum += int(code[w*2+1])
                        odd_sum += int(code[w*2])
                    # 10의배수면
                    if (odd_sum*3 + even_sum)%10 == 0:
                        for a in code:
                            answer += int(a)
                        return answer
                    # 10의배수가 아니면
                    else:
                        return answer
                        
    
    print(f"#{tc} {find_code()}")
                    

    