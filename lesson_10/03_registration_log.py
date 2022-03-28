# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.

# TODO здесь ваш код

import os
import os.path

class NotNameError(Exception):
    def __init__(self, input_data):
        self.input_data = input_data

    def __str__(self):
        print('Это не имя!')

class NotEmailError(Exception):
    def __init__(self, input_data):
        self.input_data = input_data

    def __str__(self):
        print('Это не почта!')

current_path = os.path.abspath(__file__)
splitted = os.path.split(current_path)
current_path = splitted[0]

input_file = os.path.join(current_path, 'registrations.txt')
output_good = os.path.join(current_path, 'registrations_good.log')
output_bad = os.path.join(current_path, 'registrations_bad.log')

class format_checker:

    def __init__(self, input_file, output_good, output_bad):
        self.inp = input_file
        self.outg = output_good
        self.outb = output_bad

    def name_checker(self, name):
        if name.isalpha() == False:
            raise NotNameError('Введено некорректное имя')

    def age_checker(self, age):
        age = int(age)
        if age < 10 or age > 99:
            raise ValueError('Введен некорректный возраст')

    def mail_checker(self, mail):
        if ('.' in mail) and ('@' in mail):
            pass
        else:
            raise NotEmailError('Введен некорректный почтовый адрес')

# версия движка с открытием, записью и моментальным закрытием выходных файлов логов. Много ресурсов ест, но можно смотреть на результаты в любой момент

    #def bad_writer(self, line, error):
    #    with open(self.outb, 'a') as out:
    #        out.write(line)
    #        for err in error:
    #            out.write(f'{err}\n\n')

    #def engine(self):
    #    inp = open(self.inp, 'r', encoding='UTF-8')
    #    for line in inp:
    #        try:
    #            name, mail, age = line.split(' ')
    #            self.name_checker(name = name)
    #            self.age_checker(age = age)
    #            self.mail_checker(mail = mail)
    #        except ValueError as exc:
    #            self.bad_writer(line, exc.args)
    #        except NotNameError as exc:
    #            self.bad_writer(line, exc.args)
    #        except NotEmailError as exc:
    #            self.bad_writer(line, exc.args)
    #        else:
    #            with open(self.outg, 'a') as out:
    #                out.write(line)
    #    inp.close()


# версия движка с открытыми все время файлами выходных логов. Код чуть больше, в процессе результаты не посмотришь, но выполняется в 5 раз быстрее

    def bad_writer(self, line, error):
        self.outb.write(line)
        for err in error:
            self.outb.write(f'{err}\n\n')

    def engine(self):
        inp = open(self.inp, 'r', encoding='UTF-8')
        self.outb = open(self.outb, 'w')
        self.outg = open(self.outg, 'w')
        for line in inp:
            try:
                name, mail, age = line.split(' ')
                self.name_checker(name = name)
                self.age_checker(age = age)
                self.mail_checker(mail = mail)
            except ValueError as exc:
                self.bad_writer(line, exc.args)
            except NotNameError as exc:
                self.bad_writer(line, exc.args)
            except NotEmailError as exc:
                self.bad_writer(line, exc.args)
            else:
                self.outg.write(line)
        inp.close()
        self.outb.close()
        self.outg.close()


# убираем все из файлов
with open(output_good, 'w') as out:
    out.write('')
    with open(output_bad, 'w') as out:
        out.write('')

test = format_checker(input_file, output_good, output_bad)
test.engine()
