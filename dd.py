# 아래 함수를 수정하시오.
def find_min_max(lst):
    # 일단 맨 앞에 있는 값을 최소값,최대값이라 생각
    min_v = lst[0]
    max_v = lst[0]

    # 최소값과 최대값을 구하는 과정
    for num in lst:
        # 지금 꺼내온 num이 min_v 보다 작다
        if num < min_v :
            min_v = num
        # 지금 꺼내온 num 이 max_v 보다 크다
        if num > max_v:
            # 발견한 더 큰 값을 최대값으로 변경
            max_v = num



    return min_v, max_v


result = find_min_max([3,1,7,2,5])
print(result) #(1,7)