import json
from typing import Dict

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


def print_movies_names(movie: Dict):
    # for key, value in movies.items():
    # for value in movies.values():
    #     print(f'Naziv filma: {value}')
    # for key in movie.keys():
    #     print(f'Naziv filma: {movie[key]}')

    print(f'Naziv filma: {movie["Title"]}')


file_content = read_json_file_content()
# print(type(file_content))
# print(file_content)


'''
2. Zadatak
    Potrenno je kreirati funkciju koja ce iz sadrzaja datoteke ispisati nazive svih filmova
'''

# for movie in file_content["movies"]:
#     print_movies_names(movie)


'''
3. Zadatak
    Ispisite naziv filma koji ima najbolju ukupnu ocjenu.
'''

max_movie_rating = 0
max_rating_movie = {}
min_movie_rating = 10
min_rating_movie = {}

for movie in file_content["movies"]:
    movie_ratings = []
    movie_rating_list = movie["Ratings"] # 9.3 / 10 ; 91% ; 81 / 100

    try:
        first_rating = movie["Ratings"][0]["Value"]
        first_rating_parts = first_rating.split('/')
        first_rating_value = float(first_rating_parts[0]) / float(first_rating_parts[1])
        movie_ratings.append(first_rating_value)
    except Exception as ex:
        pass

    try:
        second_rating_value = movie["Ratings"][1]["Value"].replace('%', '')
        second_rating_value = float(second_rating_value) / 100
        movie_ratings.append(second_rating_value)
    except Exception as ex:
        pass

    try:
        third_rating_parts = movie["Ratings"][2]["Value"].split('/')
        third_rating_value = float(third_rating_parts[0]) / float(third_rating_parts[1])
        movie_ratings.append(third_rating_value)
    except Exception as ex:
        pass

    try:
        fourth_rating_value = float(movie["Metascore"]) / 100
        movie_ratings.append(fourth_rating_value)
    except Exception as ex:
        pass

    try:
        fifth_rating_value = float(movie["imdbRating"]) / 10
        movie_ratings.append(fifth_rating_value)
    except Exception as ex:
        pass

    movie_rating = sum(movie_ratings) / len(movie_ratings)

    if movie_rating > max_movie_rating:
        max_movie_rating = movie_rating
        max_rating_movie = movie
    if movie_rating < min_movie_rating:
        min_movie_rating = movie_rating
        min_rating_movie = movie

print(max_rating_movie['Title'], max_movie_rating)
print(min_rating_movie['Title'], min_movie_rating)
