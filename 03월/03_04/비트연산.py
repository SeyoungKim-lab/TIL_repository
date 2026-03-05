decimal = 149

# 십진수를 이진수로 바꾼 결과
binary = 0

# 2로 나눈 몫이 2보다 작아질때까지 계속 나눈다.
# 나머지를 거꾸로 읽으면 이진수 완성

# 중간 나눗셈에서 나머지를 기억할 배열
arr = []

while decimal != 0:
    
    arr.append(decimal % 2)
    # 다음에 나눌 숫자는 2로 나눈 몫
    decimal = decimal//2
    
arr.reverse()
print(*arr)

# 비트연산자
def bit_print(dec):
    # dec을 2진수로 만든 결과
    output = ""
    
    for i in range(7, -1, -1):
        if dec & (1<<i):
            output += "1"
        else:
            output += "0"
    return output

print(bit_print(149))