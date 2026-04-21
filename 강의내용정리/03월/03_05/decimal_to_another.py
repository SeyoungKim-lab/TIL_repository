# 10진수를 2진수로 변환
def decimal_to_binary(n):
    binary_number = ""
    
    if n == 0:
        return 0
    
    # 0보다 클 때까지 2로 나누면서 (1. 반복을 끝내는 조건)
    # 나머지를 정답에 추가 (2. 추가구현)
    while n>0:
        # 2로 나눈 나머지를 구해서
        remain = n % 2
        # 정답에 추가
        binary_number = str(remain) + binary_number
        
        # 2로 나눈다
        n = n//2
        
    return binary_number

print(decimal_to_binary(74))


# 10진수를 16진수로 변환
def decimal_to_hexadecimal(n):
    hex_digits = "0123456789ABCDEFG"
    hexadecimal_number = ""
    
    while n>0:
        remain = n%16
        hexadecimal_number = hex_digits[remain] + hexadecimal_number
        n = n//16
    
    return hexadecimal_number


print(decimal_to_hexadecimal(16))

# 내장함수가 있기는 합니다
print(bin(5))
print(hex(255))