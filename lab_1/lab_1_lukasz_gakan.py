# Lukasz Gakan - Cwiczenie nr. 1
# Opis: Cwiczenie wporwadzajace
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def fun(x):
    return x**2 + 5


def print_triple_chart(x1, x2, x3):
    plt.plot(x1, fun(x1), color='r', label='f(x1)')
    plt.plot(x2, fun(x2), color='g', label='f(x2)')
    plt.plot(x3, fun(x3), color='b', label='f(x3)')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("f(x) = x^2 + 5")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    # zad 3
    # Polegalo na zdefiniowaniu funkcji f(x)=x^2+5 oraz sporzadzeniu jej wykresu dla podanych przedzialow
    x_1 = np.linspace(-1, 1, 100)
    x_2 = np.linspace(-6, 6, 100)
    x_3 = np.linspace(0, 5, 100)
    print_triple_chart(x_1, x_2, x_3)

    # zad 4
    # Polegalo na stworzeniu prostego dataframe za pomoca biblioteki pandas
    col_names = ['name', 'surname', 'age', 'sex']
    records = []
    for i in range(1, 6):
        records.append([f'name_'+str(i), f'surname_' + str(i), 6*i, 'male'])
    df = pd.DataFrame(records, columns=col_names)

    # Wypisanie typów zmiennych ktore sa przechowywane w dataframe
    print("df types:")
    print(df.dtypes)
    # Wypisanie informacji o danych
    print('df info:')
    print(df.info())
    # Wypisanie opisu danych
    print('df describe:')
    print(df.describe())
    # Wypisanie 3 pierwszych rekordow dataframe
    print('df head:')
    print(df.head(3))
