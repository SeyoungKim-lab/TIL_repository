import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, 1+T):
    N , hexadecimal = input().split()
    N = int(N)


    def hex_to_binary(hexa):
        
        binary = ""
        for c in hexa:
            dec = int(c,16)
            for i in range(3,-1,-1):
                binary += "1" if dec & 1<<i else "0" 
            
        return binary


    binary_num = hex_to_binary(hexadecimal)
    print(f"#{tc} {binary_num}")
