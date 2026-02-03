def countingsort(arr,n,k):
    # arr : 길이n, 정렬할 배열(원소는 0이상 k이하의 정수)

    # 정렬 결과를 저장할 배열
    sorted_arr = [0] * n

    # 숫자의 등장 횟수를 세서 저장할 카운팅 배열
    counts = [0] *(k+1)
    # arr 안에 있는 0의개수, 1의개수, ... , k의개수
    # counts[0] : 0의개수
    # counts[1] : 1의개수
    #...
    # counts[k] : k의개수

    # 1. arr 안에 있는 숫자들의 등장횟수(개수) 세기
    for i in range(n) :
        # i번 인덱스에 있는 숫자를 x 라고 하자
        x = arr[i]
        # x의 개수를 1 증가 시켜줘야 한다.
        counts[x] += 1


    # 2. counts배열의값 조정(누적합)
    # 카운팅정렬의 원리는 숫자의 자리를 배치하는 것
    # 어떤 숫자 x가 있을때, x보다 작거나 같은 숫자의 개수를 알고 있다면
    # x는 그 갯수만큼의 인덱스 위치에 놓으면 된다.
    # 1이 2개, 2가 1개, 3이 1개, 4가 2개
    # 4는 어디에 놓아야 될까?
    # 4보다 작거나 같은 숫자가 6개 6번째 위치부터 4를 놓으면 된다.
    # 인덱스는 0부터 시작하고, 같은숫자가 여러번 등장하니 다음4를 위해 -1씩 감소
    # 각 숫자의 정렬후 위치를 계산하기 위해 누적합을 구해나간다.
    for i in range(1, k+1):
        # 숫자 i보다 같거나 작은 숫자의 개수
        counts[i] += counts[i -1]

    # 3. counts 배열을 참고해서 각 숫자의 자리 배치시작(정렬)
    # 안정정렬을 위해서 뒤에서부터 배치
    for i in range(n-1, -1, -1):
        # arr 에 있는 i번째 숫자를 x라고 하면
        x = arr[i]
        counts[x] -= 1
        # 1 감소한 위치에 x를 놓는다.
        sorted_arr[counts[x]] = x

    return sorted_arr

data = [0,4,1,3,1,2,4,1]
print(countingsort(data, len(data), max(data)))