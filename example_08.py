'''
Za svaki film u json file listi ispisite naziv
    te prije koliko godina, mjeseci i dana je napravljen.
'''
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta
from example_07 import read_json_file_content


file_content = read_json_file_content()

today = dt.today()

oldest_movie = {}
oldest_movie_date = dt.today()


for movie in file_content["movies"]:
    movie_title = movie['Title']
    movie_released_date = movie['Released']

    movie_released_dt = dt.strptime(movie_released_date, '%d %b %Y')
    date_delta = relativedelta(today, movie_released_dt)

    if movie_released_dt < oldest_movie_date:
        oldest_movie = movie
        oldest_movie_date = movie_released_dt
        oldest_movie['released_before'] = date_delta

    print(f'Film "{movie_title}", je izdan prije {date_delta.years} godina, {date_delta.months} mjeseci i {date_delta.days} dana')

print()
print(f'Najsatriji film je {oldest_movie['Title']}, izdan je prije {oldest_movie['released_before'].years} godine')
