import pandas as pd
import numpy as np
import sys


def first():
    # 1.1
    titanic = pd.read_csv("titanic.csv")

    # 1.3
    N = 10
    print(f"Первые {N} строк")
    print(titanic.head(N))
    print("==========================")

    # 1.4
    COL = "Age"
    print(f"Базовая статистика по столбку {COL}")
    print(titanic[COL].describe())
    print("==========================")

    # 1.5
    print("Кол-во заголовков и кол-во строк")
    cols = len(titanic.columns)
    rows = int(titanic.size / len(titanic.columns))
    print(cols, rows)
    print("==========================")

    # 1.2
    count_cols = titanic.count()

    for i, j in count_cols.items():
        print(f"{rows - j} пропусков у {i}")

    print("Название столбца и его категория")
    print(titanic.dtypes)
    print("==========================")

    # 1 extra
    holes = titanic["Age"].isnull().sum()
    avg_age = titanic["Age"].mean()
    for i in range(len(titanic)):
        if pd.isnull(titanic.loc[i, "Age"]):
            titanic.loc[i, "Age"] = avg_age

    print("Количество пропусков в Age до и после")
    print(f"{holes} {titanic['Age'].isnull().sum()}")
    print("==========================")


def second():
    titanic = pd.read_csv("titanic.csv")

    male = titanic[titanic["Sex"] == "male"]
    female = titanic[titanic["Sex"] == "female"]

    # 2.1

    # Для мужчин
    a = male[male["Survived"] == 1]
    b = male[male["Survived"] == 0]
    c = a.shape[0] / male.shape[0] * 100
    d = male["Age"].mean()
    e = a["Age"].mean()
    f = b["Age"].mean()

    print("Мужчины:")
    print(f"% выживших: {c}")
    print(f"Средний возраст: {d}")
    print(f"Средний возраст выживших: {e}")
    print(f"Средний возраст погибших: {f}")
    print("==========================")

    # Для женщин
    a = female[female["Survived"] == 1]
    b = female[female["Survived"] == 0]
    c = a.shape[0] / female.shape[0] * 100
    d = female["Age"].mean()
    e = a["Age"].mean()
    f = b["Age"].mean()

    print("Женщины:")
    print(f"% выживших: {c}")
    print(f"Средний возраст: {d}")
    print(f"Средний возраст выживших: {e}")
    print(f"Средний возраст погибших: {f}")
    print("==========================")

    # 2.2

    print("Мужчины старше 30 лет, путешествующие первым классом:")
    mo301st = male[(male["Age"] > 30) & (male["Pclass"] == 1)]
    print(mo301st)
    print("==========================")

    print("Женщины моложе 18 лет или выживши женщины:")
    wu18s = female[(female["Age"] < 18) | (female["Survived"] == 1)]
    print(wu18s)
    print("==========================")

    grouped = titanic.groupby(["Pclass", "Sex"]).agg(
        mean_age=("Age", "mean"),
        survived_rate=("Survived", "mean"),
        mean_fare=("Fare", "mean"),
    )
    print("Группировка по классу и полу:")
    print(grouped)
    print("==========================")


first()
second()

# 3
with open("output.txt", "w") as f:
    sys.stdout = f
    pd.set_option("display.max_rows", None)
    first()
    second()
