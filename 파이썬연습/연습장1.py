import sys
sys.stdin = open('input.txt', 'r')

T= int(input())

for tc in range(1, 1+T):
    short_str = input()
    long_str = input()

    max_cnt = 0

    short_count = [0] * 26
    long_count = [0] * 26

    for s in short_str:
        short_count[ord(s)-65] = 1
    
    for l in long_str:
        if short_count[ord(l)-65] == 1:
            long_count[ord(l)-65] += 1
        max_cnt = max(max_cnt, long_count[ord(l)-65])

    print(f"#{tc} {max_cnt}")