import json

'''
1. Zadatak - Potrebno je ucitati podatke iz datoteke movies-250.json i ispisite sadrzaj u konzoli.
'''

# datoteka = open('data/movies-250.json', 'r')
# sadrzaj_datoteke = datoteka.read()
# print(sadrzaj_datoteke)
# datoteka.close()


def read_json_file_content(file_path = 'data/movies-250.json'):
    try:
        with open(file_path, 'r') as file_reader:
            # file_content = file_reader.read()
            # print(file_content)
            # return file_reader.read()
            json_file_content = json.load(file_reader)
            return json_file_content

    except Exception as ex:
        print(f'Dogodila se greska {ex}.')
        return ''



file_content = read_json_file_content()
# print(type(file_content))
# print(file_content)


'''
2. Zadatak
    Potrenno je kreirati funkciju koja ce iz sadrzaja datoteke ispisati nazive svih filmova
'''

