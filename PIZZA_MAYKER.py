names = []
ages = []
order = []
size_pizza_18 = []
size_pizza_17 = []
pizza_18 = []
pizza_17 = []
total_price = []

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
                    order.append("пеперони")
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
                    order.append("гавайская")
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
                    break
                elif menu2 == "сырная":
                    order.append("сырная")
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
                    break
                else:
                    print("Введите 'пеперони', 'гавайская' или 'сырная'")
                    continue
            break
        elif menu == "свою":
            def size_pizza(): #в этой функции срашивается о размере пиццы
                while True:
                    print("Какой размер(15см, 20см, 25см, 30см, 35см) \n")
                    size_pizza = int(input())
                    if size_pizza == 15:
                        print("Какие вы хотитите ингридиенты?")
                        size_pizza_18.append(size_pizza)
                        break
                    elif size_pizza == 20:
                        print("Какие вы хотитите ингридиенты?")
                        size_pizza_18.append(size_pizza)
                        break
                    elif size_pizza == 25:
                        print("Какие вы хотитите ингридиенты?")
                        size_pizza_18.append(size_pizza)
                        break
                    elif size_pizza == 30:
                        print("Какие вы хотитите ингридиенты?")
                        break
                    elif size_pizza == 35:
                        print("Какие вы хотитите ингридиенты?")
                        size_pizza_18.append(size_pizza)
                        break

            size_pizza()
            def custom_pizza():
                    print(      "Выберите ингридиенты: \n"
                                "Тесто \n" #200
                                "Колбаса(пеперони или докторскую), \n" #150
                                "Сыр(Моццарела или пормезан) \n" #100
                                "Холпенье \n" #50
                                "Ананасы \n" #150
                                "Кетчуп \n" #100
                        )
                    fl = True
                    try:
                        while fl:
                            custom_pizza = input()
                            order.append(custom_pizza)
                            print("Вы хотите ещё ингридиенты?")
                            stop_custom = input()
                            if stop_custom == "нет":
                                fl = False
                            elif stop_custom == "да":
                                fl = True
                    except "нет":
                        fl = False
                        print("Хороший выбор")
            custom_pizza()
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
print("Введите ваше фамилию, имя, отчество")
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
        print("Всё верно? да или нет")
        yes_no = input()
        if yes_no == "да":
            break
        elif yes_no == "нет":
            print("Вы хотите что то удалить или добавить? 1 - добавить; 2 - удалить")
            delsoradd = int(input())
            if delsoradd == 2:
                def dels_17():
                    try:
                        f2 = True
                        while f2:
                            print(order)
                            delses = input()
                            if delses == "сок":
                                order.remove("сок")

                            elif delses == "вода":
                                order.remove("вода")

                            elif delses == "минеральная вода":
                                order.remove("минеральная вода")

                            elif delses == "чай":
                                order.remove("чай")
                            print(f"Вы хотите ещё чтото убрать? {order} 1 - да; 2 - нет (выбрать цифру)")
                            stop = int(input())
                            if stop == 2:
                                f2 = False
                            elif stop == 1:
                                f2 = True
                            else:
                                continue
                    except 2:
                        f2 = False
                        print("Сейчас подсчитаем итогувую цену")

                dels_17()
            elif delsoradd == 1:
                print("Что вы хотите добавить")
                def add():
                    while True:
                        print("пицца или напиток?")
                        a = input()
                        if a == "пицца":
                            def add_1():
                                try:
                                    while True:
                                        print("Какую пиццу вы хотите? \n"
                                              "пеперони \n"
                                              "гавайская \n"
                                              "сырная \n")
                                        add_1 = input()
                                        if add_1 == "пеперони":
                                            order.append("пеперони")
                                            break
                                        elif add_1 == "гавайская":
                                            order.append("гавайская")
                                            break
                                        elif add_1 == "сырная":
                                            order.append("сырная")
                                            break
                                        else:
                                            continue
                                    while True:
                                        print("Хотите ещё добавить пиццу? 1 - да; 2 - нет")
                                        yesorno = int(input())
                                        if yesorno == 1:
                                            f2 = True
                                        elif yesorno == 2:
                                            f2 = False
                                except 2:
                                    f2 = False
                            add_1()
                            break
                        elif a == "напиток":
                            def add_2():
                                try:
                                    while True:
                                        print("1 - сок \n"
                                      "2 - вода \n"
                                      "3 - минеральная вода \n"
                                      "4 - чай \n ")
                                        b = int(input())
                                        if b == 1:
                                            order.append("сок")
                                            break
                                        elif b == 2:
                                            order.append("вода")
                                            break
                                        elif b == 3:
                                            order.append("минеральная вода")
                                            break
                                        elif b == 4:
                                            order.append("чай")
                                            break
                                        else:
                                            continue
                                        while True:
                                            print(f"Вы хотите что то добавить? {order} 1 - да; 2 - нет")
                                            stoping = int(input())
                                            if stoping == 1:
                                                continue
                                            elif stoping == 2:
                                                break
                                            else:
                                                continue
                                except 2:
                                    f5 = False
                            add_2()
                            break
                        else:
                            continue
                add()
            break
        else:
            print("Всё верно 'да' или 'нет' ")
            continue
def name(): #в функции запрашивает имя
    name = input()
    names.append(name)
name()
print("Какой ваш возврост?")
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
            verefy_order()
            break
        else:
            print("Введите сколько вам лет")
age()
def mathorder():
    f"ketchup: {100}"
    f"chesse = {100}"
    f"pineapples = {150}"
    f"meat = {150}"
    f"dough = {200}"
    f"serfdom = {50}"
    f"sprite = {100}"
    f"coco_cola {100}"
    f"juice = {100}"

    print(total_price)
mathorder()