import sys
sys.stdin = open("mst_input.txt", "r")

# TODO : x가 속한 집합의 대표찾기 함수

    # x의 부모가 자기자신이면(=x가 속한 집합의 대표가 x이면)
    
        # 대표를 리턴
        
    # 경로 압축: x의 부모 자리에 x부모의 find_set을 넣는다.
    
    # x부모를 리턴
    

# TODO : x가속한집합, y가속한집합을 합치는 함수

    # x의 대표찾고 변수로 두기
    
    # y의 대표찾고 변수로 두기
    
    # 대표가 같으면 유니온 할 필요 X
    
    # 더 작은 대표로 통일해서 병합하기
    
        
    

# TODO : V,E 입력받기


# 1. 간선들을 가중치 기준으로 정렬
# TODO : edges 리스트 만들기


# TODO : E번 입력 받아 (start,end,weight)를 edges에 담기


# TODO : 가중치 기준 오름차순 정렬



# 2. 가중치가 작은 간선부터 순서대로 선택하자
#  - 사이클이 발생하면 고르지 말자!
#  - 언제까지 ?
#   - MST 가 완성될 때까지
#   - == V-1 개를 선택할 때 까지
# TODO : 현재까지 선택한 간선의 수 cnt 변수로두기

# TODO : 가중치의 합 result 변수로두기

# TODO : make_set: parents 리스트형성

# TODO : edges 순회하며 집합 합치기

    # u, v가 사이클이 아니라면 유니온하라
    
        # union
        
        # cnt 증가
        
        # result 증가
        
        # 종료조건
        

print(f'최소 비용 = {result}')


