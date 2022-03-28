# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.

# TODO здесь ваш код

from random import randint
import os
import os.path

ENLIGHTENMENT_CARMA_LEVEL = 777
total_karma = 0

# находим путь к исполняемому файлу и указываем, куда будем сохранять лог 
file = os.path.abspath(__file__)
splitted = os.path.split(file)
file = os.path.join(splitted[0], 'one_day_log.txt')

# создаем все нужные виды ошибок с одной переменной для хранения информации об ошибке, которая сохраянется при ее вызове
class IamGodError(Exception):
    def __init__(self, input_data = None):
        self.message = 'Я Бог!'
        self.input_data = input_data

    def __str__(self):
        return self.message

class DrunkError(Exception):
    def __init__(self, input_data = None):
        self.message = 'Я напился'
        self.input_data = input_data

    def __str__(self):
        return self.message

class CarCrashError(Exception):
    def __init__(self, input_data = None):
        self.message = 'Меня сбила машина'
        self.input_data = input_data

    def __str__(self):
        return self.message

class GluttonyError(Exception):
    def __init__(self, input_data = None):
        self.message = 'Я глютен :)'
        self.input_data = input_data

    def __str__(self):
        return self.message

class DepressionError(Exception):
    def __init__(self, input_data = None):
        self.message = 'Я в депрессии'
        self.input_data = input_data

    def __str__(self):
        return self.message

class SuicideError(Exception):
    def __init__(self, input_data = None):
        self.message = 'Я самоубился'
        self.input_data = input_data

    def __str__(self):
        return self.message

# случайное число кармы начисляется вне зависимости от наличия ошибки, следовательно, просто возвращаем рандинт от одного до семи
def one_day():
    karma = randint(1, 7)
    flag = randint(1, 13)
    if flag == 13:
        exc_numb = randint(1, 6)
        if exc_numb == 1:
            try:
                raise IamGodError('Я Бог!')
            except IamGodError as exc:
                with open(file, 'a') as ff:
                    for arg in exc.args:
                        ff.write(f'{arg}\n')
        if exc_numb == 2:
            try:
                raise DrunkError('Я напился')
            except DrunkError as exc:
                with open(file, 'a') as ff:
                    for arg in exc.args:
                        ff.write(f'{arg}\n')
        if exc_numb == 3:
            try:
                raise CarCrashError('Меня сбила машина!')
            except CarCrashError as exc:
                with open(file, 'a') as ff:
                    for arg in exc.args:
                        ff.write(f'{arg}\n')
        if exc_numb == 4:
            try:
                raise GluttonyError('Я глютен :)')
            except GluttonyError as exc:
                with open(file, 'a') as ff:
                    for arg in exc.args:
                        ff.write(f'{arg}\n')
        if exc_numb == 5:
            try:
                raise DepressionError('Я в депрессии')
            except DepressionError as exc:
                with open(file, 'a') as ff:
                    for arg in exc.args:
                        ff.write(f'{arg}\n')
        if exc_numb == 6:
            try:
                raise SuicideError('Я самоубился')
            except SuicideError as exc:
                with open(file, 'a') as ff:
                    for arg in exc.args:
                        ff.write(f'{arg}\n')

    return karma

# перезаписываем файл заново, если он уже есть
with open(file, 'w') as ff:
    ff.write('Starting new model\n')

# оборациваем в цикл выполнение функции и запись кармы
while total_karma < ENLIGHTENMENT_CARMA_LEVEL:
    total_karma += one_day()
    print(total_karma)
    with open(file, 'a') as ff:
        ff.write(f'Karma level = {total_karma}\n')


# https://goo.gl/JnsDqu



# можно было сделать лучше, как минимум - вытащить запись аргументов ошибки в цикл, туда же, где записывается уровень кармы.
# в данной версии это этого пострадала только читаемость кода, т.к. ошибки не очень частые, 
# затраты ресурсов на открыть-закрыть файл не сильно изменились
