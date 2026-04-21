T = int(input())

for tc in range(1, 1+T):
    

    # hex_to_bin = {
    #     "0": "0000", "1": "0001", "2": "0010", "3": "0011", "4": "0100", "5": "0101", "6": "0110",
    #     "7": "0111", "8": "1000", "9": "1001", "A": "1010", "B": "1011", "C": "1100", "D": "1101",
    #     "E": "1110", "F": "1111"
    # }

    N , hex = input().split()

    # result = ""
    # for i in range(int(N)):
    #     result += hex_to_bin[hex[i]]

    # print(f"#{tc} {result}")

    result2 = ""
    for c in hex:
        # c를 숫자로 바꾸고
        dec = int(c, 16)

        result_bin = ""

        # 2진수 * 4
        for i in range(3, -1, -1):
            result_bin += "1" if dec & (1 << i) else "0"

        result2 += result_bin

    print(result2)
