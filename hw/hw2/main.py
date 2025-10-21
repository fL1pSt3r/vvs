def level_1():
    text_1 = "прИвЕт МИР"
    method = input("Введите метод: ")
    if method == "upper":
        result = text_1.upper()
    elif method == "lower":
        result = text_1.lower()
    elif method == "capitalize":
        result = text_1.capitalize()
    print(result)


def level_2():
    text_2 = "Ботать – это круто. Очень круто!"
    method = input("Введите метод: ")
    if method == "find":
        substr = input("Введите подстроку для поиска: ")
        result = text_2.find(substr)
    elif method == "replace":
        old = input("Что заменить: ")
        new = input("На что заменить: ")
        result = text_2.replace(old, new)
    elif method == "count":
        char = input("Введите символ для подсчета: ")
        result = text_2.count(char)
    print(result)


def level_3():
    text_3 = "1,2,3,4,5,6"
    method = input("Введите метод: ").strip()
    if method == "split":
        sep = input("Введите разделитель: ")
        result = text_3.split(sep)
    elif method == "join":
        items = text_3.split(",")
        sep = input("Введите разделитель для join: ")
        result = sep.join(items)
    print(result)


def level_4():
    text_4a, text_4b, text_4c = "123456", "abc", " abc^&* "
    method = input("Введите метод: ")
    if method == "isdigit":
        result = text_4a.isdigit()
    elif method == "isalpha":
        result = (text_4b.isalpha(), text_4c.isalpha())
    elif method == "strip":
        result = text_4c.strip()
    print(result)


def level_5():
    text_5 = " python;IS;AWEsomE;! "
    stripped = text_5.strip()
    parts = stripped.split(";")
    parts[0] = parts[0].capitalize()
    parts[1] = parts[1].lower()
    parts[2] = parts[2].lower()
    result = f"{parts[0]} {parts[1]} {parts[2]}{parts[3]}"
    print(result)


print("Выберите уровень (1-5) или 0 для выхода.")
while True:
    try:
        level = int(input("Введите уровень: "))
    except ValueError:
        print("Введите число от 1 до 5.")
        continue
    if level == 0:
        print("Выход из игры.")
        break
    elif level == 1:
        level_1()
    elif level == 2:
        level_2()
    elif level == 3:
        level_3()
    elif level == 4:
        level_4()
    elif level == 5:
        level_5()
    else:
        print("Нет такого уровня.")
