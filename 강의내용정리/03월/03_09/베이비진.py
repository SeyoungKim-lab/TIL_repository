arr = list(map(int, input().split()))

def babygin_check():
    cnt = 0
    # 앞에꺼 3개체크
    a, b, c = path[0], path[1], path[2]
    if a == b == c:
        cnt += 1
    elif a == b-1 == c-2:
        cnt += 1

    # 뒤에꺼 3개체크
    a, b, c = path[3], path[4], path[5]
    if a == b == c:
        cnt += 1
    elif a == b-1 == c-2:
        cnt += 1

    return cnt == 2

def permutation(idx):
    global is_babygin
    if idx == 6:
        if babygin_check():
            is_babygin = "Babygin"
            return
        return
    
    for i in range(6):
        if visited[i]:
            continue
        visited[i] = 1
        path.append(arr[i])
        permutation(idx+1)
        path.pop()
        visited[i] = 0

is_babygin = "Nope"
visited = [0]*6
path = []
permutation(0)
print(is_babygin)