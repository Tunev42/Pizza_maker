def age():
    while True:
        age = int(input())
        if age <= 18:
            print("У вас будет неполненное меню из-за \n"
                  "того что вам ещё не исполнилось 18 лет \n")
            break
        elif age >= 18:
            print("У вас полное меню")
            break
        else:
            print("Введите сколько вам лет")
def menu():
    print("Вы хотите заказать уже созданую или свою(кастамизированную)")
    while True:
        menu = input()
        if menu == "созданую":
            print("Выберите какую: \n"
                  "Пеперони \n"
                  "Гавайская \n"
                  "Сырная \n")
        elif menu == "свою":
            print("Какой размер(15см, 20см, 25см, 30см, 35см) \n"
                  "Какие добавки: \n"
                  "Колбаса(пеперони или докторскую), \n"
                  "Сыр(Моццарела или пормезан) \n"
                  "Нужно холпенье(да или нет) \n")
            def size_pizza():
                size_pizza = int(input())
                if size_pizza == 15:
                    def custom_pizza_kolbasa():
                        custom = input()
                        print("Вам нужна колбаса")
                        if custom == "да":
                            print("Какую колбасу(пеперони или докторскую)")
                            custom1 = input()
                            if custom1 == "пеперони":
                                print("Нужен ли вам сыр?")
                            elif custom1 == "докторскую":
                                print("Нужен ли вам сыр?")


