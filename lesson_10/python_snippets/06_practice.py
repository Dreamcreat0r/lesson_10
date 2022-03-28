# -*- coding: utf-8 -*-

# Есть файл calc.txt с записями операций - текстовый калькулятор. Записи вида
#
# 100 + 34
# 23 / 4
#
# то есть ОПЕРАНД_1 ОПЕРАЦИЯ ОПЕРАНД_2, разделенные пробелами.
# Операндны - целые числа. Операции - арифметические, целочисленное деление и остаток от деления.
#
# Нужно вычислить все операции и найти сумму их результата.
import os
import os.path

def calc(line):
    # print(f'Read line {line}', flush=True)
    operand_1, operation, operand_2 = line.split(' ')
    operand_1 = int(operand_1)
    operand_2 = int(operand_2)
    if operation == '+':
        value = operand_1 + operand_2
    elif operation == '-':
        value = operand_1 - operand_2
    elif operation == '/':
        value = operand_1 / operand_2
    elif operation == '*':
        value = operand_1 / operand_2
    elif operation == '//':
        value = operand_1 // operand_2
    elif operation == '%':
        value = operand_1 % operand_2
    else:
        raise ValueError('Unknown operation {operation}')
    return value


path = os.path.abspath(__file__)
splitted = os.path.split(path)
path = os.path.join(splitted[0], 'calc.txt')

total = 0
with open(path, 'r') as ff:
    for line in ff:
        line = line[:-1]
        try:
            total += calc(line)
        except ValueError as exc:
            if 'unpack' in exc.args[0]:
                print(f'Не хватает операндов {exc}', end = '')
            else:
                print(f'Не могу преобразовать к целому {exc} в строке {line}', end = '')
            print(f' в строке:   {line}')

print(f'Total {total}')
