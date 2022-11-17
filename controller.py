import view
import log
import import_data
import export_data


def phone_book(login):
    ops_type = view.operation_type()
    if ops_type == '1':
        search_el = view.search_element()
        data = export_data.export_output(search_el, view.export_format(), export_data.export_data())
        view.view_data(data)
        log.log(login, 1, search_el, data)
        view.view_data('')
        phone_book(login)
    elif ops_type == '2':
        data = view.input_data()
        import_data.import_data(data)
        log.log(login, 2, data, '')
        view.view_data('Запись внесена\n')
        phone_book(login)
    else:
        view.view_data('До свидания!')
