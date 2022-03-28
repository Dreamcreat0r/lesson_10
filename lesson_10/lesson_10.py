try:
    raise NameError('Привет Там')
except NameError as exc:
    print(f'Исключение типа {type(exc)} пролетело мимо! его параметры {exc.args}')
    # обратите внимание на "пустой" оператор - будет переброшено исключение текущего скоупа.
    raise

alpha = 1
alpha += 1