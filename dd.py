list_of_book = [
    '장화홍련전',
    '가락국 신화',
    '온달 설화',
    '금오신화',
    '이생규장전',
    '만복자서포기',
    '수성지',
    '백호집',
    '원생몽유록',
    '홍길동전',
    '장생전',
    '도문대작',
    '옥루몽',
    '옥련몽',
]

rental_list = [
    '장생전',
    '원생몽유록',
    '이생규장전',
    '장화홍련전',
    '수성지',
    '백호집',
    '난중일기',
    '홍길동전',
    '만복자서포기',
]
for rental_book in rental_list:
    for list_book in list_of_book:
        if list_book == rental_book:
            break 
    break

print('모든 도서가 대여 가능한 상태입니다.')
'''
list_book==rental_book 이면 첫번째for문으로 이동
즉, 장생전 == 장화홍련전 아니니까 이때부터 바로 print를 하는상황.

for rental_book in rental_list:
    for list_book in list_of_book:
        if list_book == rental_book:
            break 
이상태면 장생전==장화홍련전 아니니까 다시 안쪽 for문 돌다가
장생전==장생전 되면 다시 바깥 for문으로 가야함. ㅇㅋ
그러다가 잘가다가 난중일기일때,
끝까지 난중일기가 없어. 그럼 탈출해야해.
난중일기==옥련몽까지 했는데 아니야. 그러면 아예 탈출해야돼



'''


'''
rental_book에 '장생전'이 할당됨
이때 장생전이 list_of_book 에 있는지 확인해야함
이걸 어떻게확인하지
if rental_book = list_of_book[0~끝] 맞는지 확인하고싶음
그러면 if문 안에서 또 반복문을 해야할듯
for list_book in list_of_book
if list_book = rental_book
break 
'''