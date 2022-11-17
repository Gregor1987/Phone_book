import datetime


def log(user_name, op_type, search_element, data):
    strr = str(f'user: {user_name}; operation: ')
    if data != 'Такой записи нет':
        if op_type == 1:
            if search_element == 'all':
                strr += 'all data extraction '
            else:
                strr += str(f'data extraction for {search_element} ')
        else:
            strr += str(f'data import; entry created for {search_element["Фамилия"]} ')

    else:
        strr += str(f'failed data extraction attempt, searched {search_element} ')
    strr += str(f'at {datetime.datetime.now()}\n')
    with open('log.txt', 'a', encoding='UTF-8') as file:
        file.write(strr)
