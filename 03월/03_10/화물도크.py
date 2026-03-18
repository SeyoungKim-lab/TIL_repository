import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, 1+T):
    N = int(input())

    activity = []

    for _ in range(N):
        s, e = map(int, input().split())
        activity.append((s,e))
    
    activity.sort(key= lambda x: x[1])

    activity_select = []
    finish_time = 0

    for s,f in activity:
        if s >= finish_time:
            activity_select.append((s,f))
            finish_time = f
    
    answer = len(activity_select)
    print(f"#{tc} {answer}")