bit = "00000010001101"

# 이진수를 7칸씩 쪼개서 쪼갠 것들 각각 십진수로 바꾸기
N = len(bit)

# 길이가 14
# 0~6
# 7~13
for i in range(0, N, 7):
    # i번 비트에서 7칸 짤라서 십진수로 만들고 출력
    decimal = 0
    
    # ex) bin = 0000001
    # decimal += bin[6] * 2**0
    # decimal += bin[5] * 2**1
    # decimal += bin[4] * 2**2
    #...
    # decimal += bin[0] * 2**6
    
    ith_bin = bit[i:i+7]
    
    for k in range(6,-1,-1):
        decimal += int(ith_bin[k]) * 2**(6-k)
        
    print(decimal, ",")