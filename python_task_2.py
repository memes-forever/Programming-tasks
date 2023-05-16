"""
Python Task 2
Даны два массива:
    a = [1, 2, 3, 2, 0]
    b = [5, 1, 2, 7, 3, 2]
Надо вернуть пересечение множеств с повторением элементов:
    z = [1, 2, 2, 3]
"""


def array_cross(a_list: list, b_list: list) -> list:
    z = []
    # перебираем все элементы из списка a
    for value in a_list:
        # проверяем наличие в списке b
        if value in b_list:
            z.append(value)  # добавляем
    z.sort()  # сортируем получившийся список
    return z


if __name__ == '__main__':
    a = [1, 2, 3, 2, 0]
    b = [5, 1, 2, 7, 3, 2]
    print(array_cross(a, b))
