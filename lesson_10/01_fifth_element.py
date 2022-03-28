# -*- coding: utf-8 -*-

# Умножить константу BRUCE_WILLIS на пятый элемент строки, введенный пользователем

BRUCE_WILLIS = 42

def frac():
    input_data = input('Если хочешь что-нибудь сделать, сделай это сам: ')
    try:
        leeloo = int(input_data[4])
        result = BRUCE_WILLIS * leeloo
        print(f"- Leeloo Dallas! Multi-pass № {result}!")
    except ValueError as val:
        print(f'Ошибка, введите цифры {val.args}')
        frac()
    except IndexError as ind:
        print(f'Ошибка, введите минимум 5 цифер {ind.args}')
        frac()
    except:
        print('Неизвестная ошибка')

frac()
# Ообернуть код и обработать исключительные ситуации для произвольных входных параметров
# - ValueError - невозможно преобразовать к числу
# - IndexError - выход за границы списка
# - остальные исключения
# для каждого типа исключений написать на консоль соотв. сообщение




