import sys
sys.stdin = open("input.txt" , "r")

arr = list(map(int, input().split()))

def merge_sort(start, end):
    # 1. 종료조건
    if start == end - 1:    # 한개만남으면
        return start, end
    # 2. 재귀호출
    mid = (start+end) // 2
    # 왼쪽부분
    left_s, left_e = merge_sort(start, mid)
    # 오른쪽부분
    right_s, right_e = merge_sort(mid, end)
    # 합치기
    merge(left_s, left_e, right_s, right_e)
    return start, end

def merge(left_s, left_e, right_s, right_e):
    pass

    