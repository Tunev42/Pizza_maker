import re
names = []
ages = []
order = []
size_pizza_18 = []
size_pizza_17 = []
pizza_18 = []
pizza_17 = []
total_price = []
number = []
def menu_18(): #в этой функции мы создаём меню 18+
    print("Вы хотите заказать уже созданую или свою")
    while True:
        menu = input()
        if menu == "созданую": # тут запрашивается созданные пиццы или свою, тоесть создать свою
            print("Выберите какую: \n"
                  "Пеперони: \n"
                  "Пеперони, сыр(на выбор), кетчуп и добавки на выбор \n"
                  "Гавайская: \n"
                  "Ананасы, кетчуп, сыр(на выбор) и добавки на выбор.\n"
                  "Сырная: \n"
                  "Сыр(на выбор), кутчуп и добавки на выбор. \n")
            while True:
                menu2 = input()
                if menu2 == "пеперони":
                    order.append("пицца пеперони")
                    while True:
                        print("Какой размер вы хотите 15, 20, 25 или 30")
                        size_18 = int(input())
                        if size_18 == 15:
                            size_pizza_18.append(size_18)
                            break
                        elif size_18 == 20:
                            size_pizza_18.append(size_18)
                            break
                        elif size_18 == 25:
                            size_pizza_18.append(size_18)
                            break
                        elif size_18 == 30:
                            size_pizza_18.append(size_18)
                            break
                        else:
                            print("Введите заново")
                            continue
                    order.append(menu2)
                elif menu2 == "гавайская":
                    order.append("пицца гавайская")
                    while True:
                        print("Какой размер вы хотите 15, 20, 25 или 30")
                        size_18 = int(input())
                        if size_18 == 15:
                            size_pizza_18.append(size_18)
                            break
                        elif size_18 == 20:
                            size_pizza_18.append(size_18)
                            break
                        elif size_18 == 25:
                            size_pizza_18.append(size_18)
                            break
                        elif size_18 == 30:
                            size_pizza_18.append(size_18)
                            break
                        else:
                            print("Введите заново")
                            continue
                    break
                elif menu2 == "сырная":
                    order.append("пицца сырная")
                    while True:
                        print("Какой размер вы хотите 15, 20, 25 или 30")
                        size_18 = int(input())
                        if size_18 == 15:
                            size_pizza_18.append(size_18)
                            break
                        elif size_18 == 20:
                            size_pizza_18.append(size_18)
                            break
                        elif size_18 == 25:
                            size_pizza_18.append(size_18)
                            break
                        elif size_18 == 30:
                            size_pizza_18.append(size_18)
                            break
                        else:
                            print("Введите заново")
                            continue
                    break
                else:
                    print("Введите 'пеперони', 'гавайская' или 'сырная'")
                    continue
            break
        elif menu == "свою":
            def custom_pizza():
                order.append("тесто")
                while True:
                    print("Выберите ингредиенты: \n"
                          "Колбаса - 1, \n"  # 150
                          "Сыр - 2 \n"  # 100
                          "Холопенье - 3 \n"  # 50
                          "Ананасы - 4 \n"  # 150
                          "Кетчуп - 5 \n")  # 100
                    try:
                        custom_pizza = int(input())
                        if custom_pizza == 1:
                            order.append("колбаса")
                        elif custom_pizza == 2:
                            order.append("сыр")
                        elif custom_pizza == 3:
                            order.append("холопенье")
                        elif custom_pizza == 4:
                            order.append("ананасы")
                        elif custom_pizza == 5:
                            order.append("кетчуп")
                        else:
                            print("Неверный выбор. Попробуйте снова.")
                            continue
                        print("Вы хотите ещё ингредиенты? 1 - да; 2 - нет")
                        stop_custom = int(input())
                        if stop_custom == 2:
                            break
                    except ValueError:
                        print("Ошибка ввода. Введите число.")
                return order
            def size_pizza():  # в этой функции срашивается о размере пиццы
                while True:
                    print("Какой размер(15см, 20см, 25см, 30см) \n")
                    size_pizza = int(input())
                    if size_pizza == 15 or 20 or 25 or 30:
                        size_pizza_18.append(size_pizza)
                        break
                    else:
                        continue
            custom_pizza()
            size_pizza()
def menu_17():
    print("У вас сокращённое меню")
    fl = True
    while fl:
        print("Какую пиццу вы хотите? \n"
              "пеперони \n"
              "гавайская \n"
              "сырная \n")
        menu_17_pizza = input()
        if menu_17_pizza == "пеперони":
            order.append("пицца пеперони")
            print("Какой размер пиццы")
            while fl:
                print("15 или 20 см")
                size_17 = int(input())
                if size_17 == 15:
                    size_pizza_17.append(size_17)
                    break
                elif size_17 == 20:
                    size_pizza_17.append(size_17)
                    break
                else:
                    print("Введите заново")
                    continue
            break
        elif menu_17_pizza == "гавайская":
            order.append("гавайская пицца")
            print("Какой размер пиццы")
            while fl:
                size_17 = int(input())
                print("15 или 20 см")
                if size_17 == 15:
                    size_pizza_17.append(size_17)
                    break
                elif size_17 == 20:
                    size_pizza_17.append(size_17)
                    break
                else:
                    print("Введите заново")
                    continue
            break
        elif menu_17_pizza == "сырная":
            order.append("сырная пицца")
            print("Какой размер пиццы")
            while fl:
                print("15 или 20 см")
                size_17 = int(input())
                if size_17 == 15:
                    size_pizza_17.append(size_17)
                    break
                elif size_17 == 20:
                    size_pizza_17.append(size_17)
                    break
                else:
                    print("Введите заново")
                    continue
            break
def drinks_18():
    print("Вы хотите напитки?(-ок)")
    drink = input()
    cola = "кола"
    juice = "сок"
    sprite = "спрайт"
    fanta = "фанта"
    f1 = True
    try:
        while f1:
            if drink == "да":
                print("Какой напиток вы хотите: \n"
                      "Кола - 1, \n"
                      "Сок - 2, \n"
                      "Спрайт - 3, \n"
                      "Фанта - 4 \n")
                vs = int(input())
                if vs == 1:
                    order.append(cola)
                elif vs == 2:
                    order.append(juice)
                elif vs == 3:
                    order.append(sprite)
                elif vs == 4:
                    order.append(fanta)
                else:
                    print("Введите 1, 2, 3, или 4")
                print("Вы хотите ещё напиток(-ки) 1-да 2- нет")
                vs1 = int(input())
                if vs1 == 1:
                    f1 = True
                elif vs1 == 2:
                    f1 = False
            else:
                f1 = False
    except 2:
        f1 = False
def drinks_17():
    print("Вы хотите напитки?(-ок)")
    drinks_171 = input()
    while True:
        if drinks_171 == "да":
            fl = True
            try:
                while fl:
                    print("1 - сок \n"
                          "2 - вода \n"
                          "3 - минеральная вода \n"
                          "4 - чай \n ")
                    drinks_17w = int(input())
                    if drinks_17w == 1:
                        order.append("сок")
                        break
                    elif drinks_17w == 2:
                        order.append("вода")
                        break
                    elif drinks_17w == 3:
                        order.append("минеральная вода")
                        break
                    elif drinks_17w == 4:
                        order.append("чай")
                        break
                    else:
                        continue
                print("Вы хотите ещё напитки? 1 - да; 2 - нет")
                yesorno = int(input())
                if yesorno == 1:
                    continue
                elif yesorno == 2:
                    break
            except 2:
                fl = False
def verefy_order_17():
    while True:
        print("Всё верно?")
        yes_no = input()
        if yes_no == "да":
            break
        elif yes_no == "нет":
            print("Вы хотите что то удалить или добавить? 1 - добавить; 2 - удалить")
            delsoradd = int(input())
            if delsoradd == 2:
                def dels_17():
                        print("Что вы хотите убрать")
                        try:
                            f2 = True
                            while f2:
                                delses = input()
                                if delses == "сок":
                                    order.remove("сок")
                                    break
                                elif delses == "вода":
                                    order.remove("вода")
                                    break
                                elif delses == "минеральная вода":
                                    order.remove("минеральная вода")
                                    break
                                elif delses == "чай":
                                    order.remove("чай")
                                    break
                                elif delses == "пицца пеперони":
                                    order.remove("пицца пеперони")
                                    break
                                elif delses == "пицца гавайская":
                                    order.remove("пицца гавайская")
                                    break
                                elif delses == "пицца сырная":
                                    order.remove("пицца сырная")
                                    break
                                else:
                                    continue
                            print("Вы хотите ещё чтото убрать? 1 - да; 2 - нет (выбрать цифру)")
                            stop = int(input())
                            if stop == 2:
                                f2 = False
                            elif stop == 1:
                                f2 = True
                        except 2:
                            print("Сейчас подсчитаем итогувую цену")
                            f2 = False
                dels_17()
            elif delsoradd == 1:
                print("Что вы хотите добавить \n"
                      "пиццу: \n"
                      "пеперони - 1 \n"
                      "гавайская - 2 \n"
                      "сырная - 3 \n"
                      "напиток: \n"
                      "сок - 4 \n"
                      "вода - 5 \n"
                      "минеральная вода - 6 \n"
                      "чай - 7 \n")
                def add():
                    try:
                        while True:
                            add_1 = int(input())
                            if add_1 == 1:
                                    order.append("пеперони")
                                    break
                            elif add_1 == 2:
                                    order.append("гавайская")
                                    break
                            elif add_1 == 3:
                                    order.append("сырная")
                                    break
                            elif add_1 == 4:
                                    order.append("сок")
                                    break
                            elif add_1 == 5:
                                    order.append("вода")
                                    break
                            elif add_1 == 6:
                                    order.append("минеральная вода")
                                    break
                            elif add_1 == 7:
                                    order.append("чай")
                                    break
                            else:
                                    continue
                        print("Хотите ещё что-то добавить 1 - да; 2 - нет")
                        stops = int(input())
                        if stops == 1:
                            f4 = True
                        elif stops == 2:
                            f4 = False
                    except 2:
                        f4 = False
                add()
            break
        else:
            print("Всё верно 'да' или 'нет' ")
            continue
def verefy_order_18():
    while True:
        print(f"Верно ли наш официант всё записали? {order} 1 - да; 2 - нет")
        choice = int(input())
        if choice == 1:
            break
        elif choice == 2:
            while True:
                print("Вы хотите удалить или добавить? 1 - удалить; 2 - добавить")
                choice1 = int(input())
                if choice1 == 1:
                    try:
                        while True:
                            print("Выберите что вы хотите удалить(введите цифру) \n"
                                  " Пицца пеперони - 1 \n"
                                  "Гавайская пицца - 2 \n"
                                  "Сырная пицца - 3 \n"
                                  "Кола - 4, \n"
                                  "Сок - 5, \n"
                                  "Спрайт - 6, \n"
                                  "Фанта - 7 \n")
                            choice3 = int(input())
                            if choice3 == 1:
                                order.remove("пицца пеперони")
                                break
                            elif choice3 == 2:
                                order.remove("гавайская пицца")
                                break
                            elif choice3 == 3:
                                order.remove("сырная пицца")
                                break
                            elif choice3 == 4:
                                order.remove("кола")
                                break
                            elif choice3 == 5:
                                order.remove("сок")
                                break
                            elif choice3 == 6:
                                order.remove("спрайт")
                                break
                            elif choice3 == 7:
                                order.remove("фанта")
                                break
                            else:
                                print("Введите заново")
                                continue
                        print("Вы хотите ещё что то удалить? 1 = да хочу 2 = нет не хочу")
                        choice4 = int(input())
                        if choice4 == 1:
                            fl = True
                        elif choice4 == 2:
                            fl = False
                    except 2:
                        fl = False
                    break
                elif choice1 == 2:
                    try:
                        while True:
                            print("Выберите что вы хотите удалить(введите цифру) \n"
                                    "Пицца пеперони - 1 \n"
                                    "Гавайская пицца - 2 \n"
                                    "Сырная пицца - 3 \n"
                                    "Кола - 4, \n"
                                    "Сок - 5, \n"
                                    "Спрайт - 6, \n"
                                    "Фанта - 7 \n")
                            choice5 = int(input())
                            if choice3 == 1:
                                order.remove("пицца пеперони")
                                break
                            elif choice3 == 2:
                                order.remove("гавайская пицца")
                                break
                            elif choice3 == 3:
                                order.remove("сырная пицца")
                                break
                            elif choice3 == 4:
                                order.remove("кола")
                                break
                            elif choice3 == 5:
                                order.remove("сок")
                                break
                            elif choice3 == 6:
                                order.remove("спрайт")
                                break
                            elif choice3 == 7:
                                order.remove("фанта")
                                break
                            else:
                                print("Введите заново")
                                continue
                        fl = True
                        while fl:
                            print("Вы хотите ещё что то удалить? 1 = да хочу 2 = нет не хочу")
                            choice4 = int(input())
                            if choice4 == 1:
                                fl = True
                            elif choice4 == 2:
                                fl = False
                    except 2:
                        fl = False
                    break
                else:
                    continue
            break
        else:
            continue
def validate_fio(fio):
    pattern = r'^[А-ЯЁ][а-яё]+\s+[А-ЯЁ][а-яё]+\s+[А-ЯЁ][а-яё]+$'
    return bool(re.match(pattern, fio.strip()))
def get_fio():
    while True:
        fio = input("Введите ФИО (Фамилия Имя Отчество): ").strip()
        if validate_fio(fio):
            return fio
        else:
            print("Ошибка! Неправильный формат ФИО.")
            print("Пример правильного формата: Иванов Иван Иванович")
            print("Пожалуйста, попробуйте снова.\n")
# Использование
fio = get_fio()
def verefy_number(phone):
    cleaned_phone = re.sub(r'[^\d+]', '', phone)
    patterns = [
        r'^\+7\d{10}$',
        r'^8\d{10}$',
        r'^7\d{10}$',
    ]
    for pattern in patterns:
        if re.match(pattern, cleaned_phone):
            return True, cleaned_phone
    return False, "Неверный формат номера"
# Простой цикл проверки
while True:
    phone = input("Введите номер телефона: ")
    is_valid, result = verefy_number(phone)
    if is_valid:
        number.append(phone)
        break
    else:
        print(f"Ошибка: {result}")
        print("Примеры правильных форматов: +79123456789, 89123456789")
        print("Попробуйте еще раз...")
        continue
print("Какой ваш возвраст?")
def age():
    while True:
        age = int(input())
        if age <= 17:
            print("У вас будет неполненное меню из-за \n"
                  "того что вам ещё не исполнилось 18 лет \n")
            ages.append(age)
            menu_17()
            drinks_17()
            print(order)
            verefy_order_17()
            break
        elif age >= 18:
            print("У вас полное меню")
            ages.append(age)
            menu_18()
            drinks_18()
            print(order)
            verefy_order_18()
            break
        else:
            print("Введите сколько вам лет")
age()
def select(func):
    def wrapper(order):
        calculated_values, total = func(order)
        # Выводим каждый элемент заказа с его стоимостью
        for i, item in enumerate(order):
            print("-" * 24)
            print(f"{item} = {calculated_values[i]}")
            print("-" * 24)
        # Выводим итоговую сумму
        print("-" * 24)
        print(f"итоговая цена = {total}")
        print("-" * 24)
        return calculated_values, total
    return wrapper
@select
def mathorder_my_pizza(order):
    values = {
        'пицца пеперони': 200,
        'пицца сырная': 200,
        'пицца гавайская': 200,
        'сок': 100,
        'чай': 100,
        'вода': 50,
        'минеральная вода': 55,
        'фанта': 70,
        'кола': 70,
        'спрайт': 70,
        'тесто': 100,
        'кетчуп': 50,
        'сыр': 50,
        'холопенье': 50,
        'ананасы': 50,
        'колбаса': 50
    }
    result = []  # Список для хранения цен
    total_sum = 0
    for item in order:
        if isinstance(item, (int, float)):
            # Если элемент уже число, используем его
            result.append(item)
            total_sum += item
        elif isinstance(item, str):
            # Приводим к нижнему регистру для поиска
            item_lower = item.lower()
            if item_lower in values:
                value = values[item_lower]
                result.append(value)
                total_sum += value
            else:
                # Если элемент не найден в словаре, добавляем 0
                result.append(0)
        else:
            # Для любых других типов добавляем 0
            result.append(0)
    return result, total_sum
result = mathorder_my_pizza(order)
def pay():
    print("_____ОПЛАТА_____")
    print("Вам с собой или в зале? \n"
          "с собой - 1; \n"
          "в зале - 2 \n")
    while True:
        pays = int(input())
        if pays == 1:
            while True:
                print("Оплата картой или наличкой \n"
                      "картой - 1"
                      "наличкой - 2")
                pays1 = int(input())
                if pays1 == 1:
                    while True:
                        money = int(input(f"С вас: {total_sum}"))
                        if money >= total_sum:
                            lastmoney = total_sum - money
                            print(f"Ваша сдача: {lastmoney}")
                        break
                    break
                elif pays1 == 2:
                    while True:
                        money = int(input(f"С вас: {total_sum}"))
                        if money >= total_sum:
                            lastmoney = total_sum - money
                            print(f"Ваша сдача: {lastmoney}")
                        break
                    break
            break
        elif pays == 2:
            while True:
                print("Оплата картой или наличкой \n"
                      "картой - 1"
                      "наличкой - 2")
                pays1 = int(input())
                if pays1 == 1:
                    while True:
                        money = int(input(f"С вас: {total_sum}"))
                        if money >= total_sum:
                            lastmoney = total_sum - money
                            print(f"Ваша сдача: {lastmoney}")
                            break
                        elif money < total_sum:
                            def delite():
                                print("Хотите ли вы удалить что-то из заказа чтобы вам хватило денег на покупку?")
                                choisee = input()
                                if choisee == "да":

                    break
                elif pays1 == 2:
                    while True:
                        money = int(input(f"С вас: {total_sum}"))
                        if money >= total_sum:
                            lastmoney = total_sum - money
                            print(f"Ваша сдача: {lastmoney}")
                            break
                    break
                else:
                    continue
