# 아래 함수를 수정하시오.
def capitalize_words(m):
    list_m = m.split()
    for i in list_m:
        i[0].upper()
    a = "".join(list_m)
    return a


result = capitalize_words("hello, world!")
print(result)
