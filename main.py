names = []
ages = []
order = []
total_price = []
print("Введите ваше имя")
def name():
    name = input()
    names.append(name)
name()
print(names)
print("Какой ваш возврост?")
def age():
    while True:
        age = int(input())
        if age <= 17:
            print("У вас будет неполненное меню из-за \n"
                  "того что вам ещё не исполнилось 18 лет \n")
            ages.append(age)
            break
        elif age >= 18:
            print("У вас полное меню")
            ages.append(age)
            break
        else:
            print("Введите сколько вам лет")
age()
def menu():
    print("Вы хотите заказать уже созданую или свою")
    while True:
        menu = input()
        if menu == "созданую":
            print("Выберите какую: \n"
                  "Пеперони: \n"
                  "Пеперони, сыр(на выбор), кетчуп и добавки на выбор \n"
                  "Гавайская: \n"
                  "Ананасы, кетчуп, сыр(на выбор) и добавки на выбор.\n"
                  "Сырная: \n"
                  "Сыр(на выбор), кутчуп и добавки на выбор. \n")
            menu2 = input().lower()
            while True:
                if menu2 == "пеперони":
                    order.append(menu2)
                    break
                elif menu2 == "гавайская":
                    order.append(menu2)
                    break
                elif menu2 == "сырная":
                    order.append(menu2)
                    break
                else:
                    print("Введите 'пеперони', 'гавайская' или 'сырная'")
            break
        elif menu == "свою":
            print("Какой размер(15см, 20см, 25см, 30см, 35см) \n")
            def size_pizza():
                size_pizza = int(input())
                if size_pizza == 15:
                    print("Какие вы хотитите ингридиенты?")
                elif size_pizza == 20:
                    print("Какие вы хотитите ингридиенты?")
                elif size_pizza == 25:
                    print("Какие вы хотитите ингридиенты?")
                elif size_pizza == 30:
                    print("Какие вы хотитите ингридиенты?")
                elif size_pizza == 35:
                    print("Какие вы хотитите ингридиенты?")
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
menu()
def drinks():
    print("Вы хотите напити?")
    drink = input()
    f1 = True
    try:
        while f1:
            if drink == "да":
                print("Какой напиток вы хотите: \n"
                      "Кола, \n"
                      "Сок, \n"
                      "Спрайт, \n"
                      "Фанта. \n")
                vs = input()
                order.append(vs)
                print("Вы хотите ещё напиток(-ки) 1-да 2- нет")
                vs1 = int(input())
                if vs1 == 1:
                    f1 = True
                elif vs1 == 2:
                    f1 = False
            else:
                f1 = False
    except "нет":
        f1 = False
drinks()
print(order)
while True:
    print("Всё верно?")
    yes_no = input()
    if yes_no == "да":
        break
    elif yes_no == "нет":
        print("Вы хотите что то удалить или добавить?")
        delsoradd = input()
        if delsoradd == "удалить":
            def dels():
                try:
                    f2 = True
                    while f2:
                        delses = input()
                        order.remove(delses)
                        print("Вы хотите ещё чтото убрать?")
                        stop = input()
                        if stop == "нет":
                            f2 = False
                        elif stop == "да":
                            f2 = True
                        else:
                            continue
                except "нет":
                    f2 = False
                    print("Сейчас подсчитаем итогувую цену")
            dels()
        elif delsoradd == "добавить":
            print("Что вы хотите добавить")
        break
    else:
        print("Всё верно 'да' или 'нет' ")
        continue
drinks()
def mathorder():
    ketchup = 100
    chesse = 100
    pineapples = 150
    meat = 150
    dough = 200
    serfdom = 50
    sprite = 100
    coco_cola = 100
    juice = 100
    total_prices = order + ketchup + chesse + pineapples + meat + dough + serfdom + sprite + coco_cola + juice
    total_price.append(total_prices)
    print(total_price)
mathorder()

