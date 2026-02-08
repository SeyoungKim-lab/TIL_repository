# 오름차순 정렬된 리스트에서 사용
def binary_search(a, N, key): #key를 찾으면 인덱스, 실패하면 -1 반환
    start = 0 # 처음 start는 0번 인덱스
    end = N-1 # 처음 end는 N-1번 인덱스
    while start <= end : # 이 조건일때만 순회
            middle = (start + end) // 2 # middle은 중앙인덱스
            if a[middle] == key : # 검색 성공
                  return middle
            elif a[middle] > key : # 중앙값보다 키가 왼쪽에 있으면
                  end = middle - 1 #왼쪽 구간 선택
            else: #중앙값보다 키가 오른쪽에 있으면
                  start = middle + 1 #오른쪽구간 선택
    return -1 # start와 end가 뒤집힌경우(찾는값없으면이렇게됨)

# [1,2,3,4,5,6,7,8,9,10]
# [1,2,3,4,5,6,7,8,9]
