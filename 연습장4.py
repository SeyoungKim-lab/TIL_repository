arr = ['A', 'B', 'C', 'D', 'E']
n = len(arr)


def get_count(tar):
    cnt = 0
    for _ in range(n):
        if target & 1:
            cnt+=1
        tar = tar>>1
    return cnt
answer = 0
for target in range(1<<n):
    if get_count(target) >= 2:
        answer += 1
print(answer)
    