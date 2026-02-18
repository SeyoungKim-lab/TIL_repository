lst = [1,2,3,4,5]   # 전체집합
N = 5               # 원소의개수


def make_set(idx,selected):     # selected의 idx번째 값을 1로바꾸고, idx+1번째함수를 호출
                                # selected의 idx번째 값을 0으로바꾸고, idx+1번째함수를 호출
                                # 즉, 하나의 함수는 자기다음번째함수를 두번 호출한다.
                                # 다만 if문으로 종료지점을 정해주도록한다.,
    # 1. 종료조건                            
    if idx == N :   # 여기에 걸렸다면
                    # 이미 selected가 완성된 상태이므로, 그에 맞게 부분집합을 출력해주도록하자.
        for i in range(N):  # selected를 원소의 개수만큼 순회한다.
            if selected[i]==1:
                print(lst[i], end=" ")
        print() # for 문을 다돌았다는건, 하나의 부분집합을 출력했다. 다음 부분집합을 위해 줄바꿈을해준다.
        return  # 재귀함수의 끝맺음.
    # 2. 재귀호출
    selected[idx] = 1   # 현재위치의 값을 1로 바꿔주고
    make_set(idx+1, selected)   # 다음위치의 함수를 호출

    selected[idx] = 0   # 현재위치의 값을 0으로 바꿔주고
    make_set(idx+1, selected)   # 다음위치의 함수를 호출

make_set(0, [0]*N)