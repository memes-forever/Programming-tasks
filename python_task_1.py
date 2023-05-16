"""
Python Task 1
Нужно реализовать функцию one_edit_apart, которая проверяет, можно ли одну строку получить из другой не более,
чем за одно исправление (удаление, добавление, изменение символа).

Примеры работы функции:
    one_edit_apart("cat",   "acts") -> false
    one_edit_apart("cat",   "at"  ) -> true
    one_edit_apart("cat",   "cats") -> true
    one_edit_apart("cat",   "cut" ) -> true
    one_edit_apart("cat",   "dog" ) -> false
    one_edit_apart("catst", "cast") -> true
"""


def one_edit_apart(source_string: str, another_string: str) -> bool:
    # Если кол-во символов отличается более чем на 1, return False
    if len(source_string) - len(another_string) > 1:
        return False

    # Если другая строка длинее источника - меняем их местами
    if len(source_string) < len(another_string):
        source_string, another_string = another_string, source_string

    # Если другая строка меньше на 1 символ
    if len(source_string) - len(another_string) == 1:
        # итерируемся по строке источника
        for position in range(len(source_string)):
            # перебираем все возможные структуры слова и сравниваем
            if source_string[:position] + source_string[position + 1:] == another_string:
                return True
        return False
    else:
        # считаем количество не повторяющихся символов
        count_diff_chars = sum(1 for position in range(len(source_string))
                                  if source_string[position] != another_string[position])
        return count_diff_chars < 2  # количество не повторяющихся символов должно быть меньше 2х


if __name__ == '__main__':
    print(one_edit_apart("cat", "acts"))
    print(one_edit_apart("cat", "at"))
    print(one_edit_apart("cat", "cats"))
    print(one_edit_apart("cat", "cut"))
    print(one_edit_apart("cat", "dog"))
    print(one_edit_apart("catst", "cast"))
