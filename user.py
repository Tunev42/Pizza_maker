import re
def test_name():
    name = print(f"ФИО:", input())
    name1 = name.istitle()
    if name1 == True:
        print(re.search(r'^[А-Я][а-яё]*\s*[А-Я][а-яё]*\s*[А-Я][а-яё]*$', r'[А-Я]'))
    else:
        name.title()
        print(re.search(r'^[А-Я][а-яё]*\s*[А-Я][а-яё]*\s*[А-Я][а-яё]*$', r'[А-Я]'))
test_name()

