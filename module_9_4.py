# Задание 1: Lambda-функция
first = 'Мама мыла раму'
second = 'Рамена мало было'

# Создаем lambda-функцию для сравнения символов
compare_chars = lambda x, y: x == y
result = list(map(compare_chars, first, second))
print(result)  # [False, True, True, False, False, False, False, False, True, False, False, False, False, False]

# Задание 2: Замыкание
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as f:
            for item in data_set:
                f.write(f"{item}\n")

    return write_everything

# Пример использования функции замыкания
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# Задание 3: Класс с методом call
from random import choice

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)

# Пример использования класса
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())  # Примерный результат: Да
print(first_ball())  # Примерный результат: Нет
print(first_ball())  # Примерный результат: Наверное