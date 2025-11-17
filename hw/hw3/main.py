import random
import os

rooms = [
    "пусто",
    "сундук",  # дается вещь
    "монстр",  # потеря здоровья или
    "ключ",  # ключ к порталу
    "портал",  # выход
    "ловушка",
]  # потеря здоровья
equip = [
    "скороходы",  # проход на 2 клетки вперед
    "аптечка",  # увеличиние здоровья на 5
    "меч",
]  # для убийства монстра

N = 5


def generate_world(n: int):
    area: list = [["пусто" for _ in range(n)] for _ in range(n)]

    # Количество обьектов
    CHEST = 3
    MONSTER = 1
    KEY = 1
    PORTAL = 1
    TRAPS = 2

    def generate_object(object_k: int, name: str):
        for k in range(object_k):
            i = random.randint(0, N - 1)
            j = random.randint(0, N - 1)
            while area[i][j] != "пусто" or (i == 0 and j == 0):
                i = random.randint(0, N - 1)
                j = random.randint(0, N - 1)
            area[i][j] = name

    generate_object(CHEST, "сундук")
    generate_object(MONSTER, "монстр")
    generate_object(KEY, "ключ")
    generate_object(PORTAL, "портал")
    generate_object(TRAPS, "ловушка")

    return area


area = generate_world(N)
visible_area = [[0 for _ in range(N)] for _ in range(N)]
visible_area[0][0] = 1


def print_player_stats(health: int, inventory: list):
    print(f"Здоровье: {health}, Инвентарь: {' '.join(inventory)}")


def print_area(area: list, player_pos: list):
    for i in range(N):  # row
        for j in range(N):  # col
            if i == player_pos[0] and j == player_pos[1]:
                print("*", end=" ")
                continue

            if visible_area[i][j]:
                table = {
                    "пусто": "_",
                    "сундук": "S",
                    "монстр": "M",
                    "ключ": "K",
                    "портал": "E",
                    "ловушка": "_",
                }
                print(table[area[i][j]], end=" ")
            else:
                print("?", end=" ")
        print()


health: int = 10
pos: list = [0, 0]  # col, row
inventory: list = []

print_player_stats(health, inventory)
print_area(area, pos)

status: bool = False  # True - Win, False - Loose


def collect_item(inventory: list, item: str, method: str):
    if method == "append":
        inventory.append(item)
    elif method == "extend":
        inventory.extend([item])


def remove_item(inventory: list, method: str, item: str = ""):
    if method == "remove":
        inventory.remove(item)
    elif method == "pop":
        inventory.pop()


def sort_inventory(inventory: list, method: str):
    if method == "sort":
        inventory.sort(key=lambda x: x[0])
    elif method == "reverse":
        inventory.reverse()

    return inventory


def find_item(inventory: list, item: str, method: str):
    if method == "index":
        try:
            if inventory.index(item) != -1:
                return True
        except:
            return False
    elif method == "in":
        return item in inventory


while health > 0:
    move: str = input()
    os.system("clear")

    # Смена позиции
    if move == "W":
        next_pos = [pos[0] - 1, pos[1]]

        if next_pos[0] < 0:
            print("Вы ударились об стену!")
            health -= 1
            continue
        pos = next_pos

    elif move == "S":
        next_pos = [pos[0] + 1, pos[1]]

        if next_pos[0] > (N - 1):
            print("Вы ударились об стену!")
            health -= 1
            continue
        pos = next_pos

    elif move == "A":
        next_pos = [pos[0], pos[1] - 1]

        if next_pos[1] < 0:
            print("Вы ударились об стену!")
            health -= 1
            continue
        pos = next_pos

    elif move == "D":
        next_pos = [pos[0], pos[1] + 1]

        if next_pos[1] > (N - 1):
            print("Вы ударились об стену!")
            health -= 1
            continue
        pos = next_pos

    elif move == "Sort":
        inventory = sort_inventory(inventory, "reverse")

    # Результат позиции
    if area[pos[0]][pos[1]] == "пусто":
        ...
    elif area[pos[0]][pos[1]] == "сундук":
        item = random.choice(equip)
        equip.remove(item)
        inventory.append(item)

        if item == "аптечка":
            print("Вы вылечились")
            health += 5
            remove_item(inventory, "remove", item)

        area[pos[0]][pos[1]] = "пусто"
    elif area[pos[0]][pos[1]] == "монстр":
        if find_item(inventory, "меч", "in"):
            print("Вы победили злого дракона!")
            area[pos[0]][pos[1]] = "пусто"
        else:
            health -= 9

    elif area[pos[0]][pos[1]] == "ключ":
        collect_item(inventory, "ключ", "append")
        area[pos[0]][pos[1]] = "пусто"

    elif area[pos[0]][pos[1]] == "портал":
        if find_item(inventory, "ключ", "index"):
            status = True
            break
        else:
            print("У вас пока нет ключа для открытия портала")

    elif area[pos[0]][pos[1]] == "ловушка":
        health -= 5
        print("Вы попались на ловушку")

    visible_area[pos[0]][pos[1]] = 1
    print_player_stats(health, inventory)
    print_area(area, pos)

print("Вы выиграли" if status else "Вы проиграли")
