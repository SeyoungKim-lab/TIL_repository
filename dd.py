number_of_people = 0


def increase_user():
    global number_of_people
    number_of_people += 1


def create_user(name, age, address):
    increase_user()
    user_info = {'name': name, 'age': age, 'adress': address}
    return user_info


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

print(f'{name[0]}님 환영합니다!')
print(f'{name[1]}님 환영합니다!')
print(f'{name[2]}님 환영합니다!')
print(f'{name[3]}님 환영합니다!')
print(f'{name[4]}님 환영합니다!')



list_user = list(map(create_user, name, age, address))
print(list_user)
