number_of_book = 100




name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']



many_user = [{'이름' : '김시습' , '나이' : 20}, 
             {'이름' : '허균' , '나이' : 16},
             {'이름' : '남혜인' , '나이' : 25}
             ]

def decrease_book(d):
    return number_of_book - d




def rental_book(info):
    for name,age in info.items():
         global number_of_book
         print(f'남은 책의 수 : {decrease_book(int(age//10))}')
         print(f'{name}님이 {int(age//10)}권의 책을 대여하였습니다.')
         number_of_book = number_of_book-int(age//10)


user_info = []
for i in many_user:
    dic = {}
    dic[i['이름']] = i['나이']
    user_info.append(dic)

for name_age in user_info:
    for name,age in name_age.items():
        print(f"{name}님 환영합니다!")
    

for a in user_info:
    rental_book(a)