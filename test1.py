many_user = [{'이름' : '김시습' , '나이' : 20}, 
             {'이름' : '허균' , '나이' : 16},
             {'이름' : '남혜인' , '나이' : 25}
             ]


user_info = []
for i in many_user:
    dic = {}
    dic[i['이름']] = i['나이']
    user_info.append(dic)

print(user_info)