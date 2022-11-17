def view_data(data):
    print(data)


def log_in():
    return input('Введите ваше имя:\n')


def operation_type(message='Выберите способ взаимодействия\n'
                           'Для эскпорта данных нажмите 1\n'
                           'Для импорта данных нажмите 2\n'
                           'Для выхода введите "exit"\n'):
    op_type = input(message)
    while op_type != '1' and op_type != '2' and op_type != 'exit':
        op_type = operation_type('некорректный выбор, попробуйте еще раз\n')
    return op_type


def export_format(message='Выберите формат для экспорта данных:\n'
                          '1 - вывод в форме строки\n'
                          '2 - вывод в форме визитки\n'):
    exp_form = input(message)
    while exp_form != '1' and exp_form != '2':
        exp_form = export_format('некорректный выбор, попробуйте еще раз\n')
    return exp_form


def input_data():
    family_name = input('введите фамилию:\n')
    name = input('введите имя:\n')
    phone = input('введите номер телефона:\n')
    comment = input('введите описание:\n')
    return {'Фамилия': family_name, 'Имя': name, 'Телефон': phone, 'Описание': comment}


def search_element():
    search_el = input('введите фамилию для поиска в базе\n'
                      'для вывода всей книги введите "all"\n')
    return search_el
