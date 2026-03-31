import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1,1+T):
    N = int(input())
    chu_list = list(map(int, input().split()))
    
    