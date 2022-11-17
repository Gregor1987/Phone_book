import json


def import_data(data):
    with open('phone_directory.json', 'w+') as file:
        if file.read() != '':
            file.seek(0)
            file_data = json.load(file)
        else:
            file_data = {"phone_book": []}
        file_data["phone_book"].append(data)
        file.seek(0)
        json.dump(file_data, file, indent=3, ensure_ascii=False)
