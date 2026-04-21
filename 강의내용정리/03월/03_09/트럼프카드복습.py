def recur(idx):
    global cnt
    if idx == 5:
        if inspect():
            print(path)
            cnt += 1
        return
    
    for i in range(4):
        path.append(card[i])
        recur(idx+1)
        path.pop()


def inspect():
    if path[0] == path[1] == path[2]:
        return True
    if path[1] == path[2] == path[3]:
        return True
    if path[2] == path[3] == path[4]:
        return True
    return False

card = ['A','J','Q','K']
cnt =0
path = []
recur(0)
print(cnt)