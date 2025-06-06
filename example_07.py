'''
1. Korak - Potrebno je ucitati podatke iz datoteke movies-250.json i ispisite sadrzaj u konzoli.
'''

# datoteka = open('data/movies-250.json', 'r')
# sadrzaj_datoteke = datoteka.read()
# print(sadrzaj_datoteke)
# datoteka.close()

def read_file_content():
    try:
        with open('data/movies-250.json', 'r') as file_reader:
            file_content = file_reader.read()

            print(file_content)

    except Exception as ex:
        print(f'Dogodila se greska {ex}.')



read_file_content()
