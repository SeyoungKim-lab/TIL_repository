def binary_search(a, N, key): #key를 찾으면 인덱스, 실패하면 -1 반환
    start = 0
    end = N-1
    while start <= end :
            middle = (start + end) // 2
            if a[middle] == key : # 검색 성공
                  return middle
            elif a[middle] > key : # 찾는 값보다 크면
                  end = middle - 1 #왼쪽 구간 선택
            else: #찾는값보다 작으면
                  start = middle + 1 #오른쪽구간 선택
    return -1 # start와 end가 뒤집힌경우(찾는값없으면이렇게됨)



