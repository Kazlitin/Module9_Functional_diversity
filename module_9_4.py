# Lambda-функция:

first = 'Мама мыла раму'
second = 'Рамена мало было'

i = 0

lambda_function = lambda x, y: x[i] == y[i] if i < min(len(x), len(y)) else False

result = list(map(lambda_function, first, second))
print(result)

# Замыкание:

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        print("Это строчка")
        for item in data_set:
            print(item, end=", \n")

        with open(file_name, 'w') as f:
            for item in data_set:
                f.write(str(item) + '\n')
    return write_everything

# Пример использования функции get_advanced_writer
write = get_advanced_writer('example.txt')
write(['А', 'это', 'уже', 'число', 5, 'в', 'списке'])



# Метод __call__:

from random import choice

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())