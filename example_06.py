from typing import Dict

movies = [
    {"Title":"The Shawshank Redemption","Year":"1994","Rated":"R","Released":"14 Oct 1994","Runtime":"142 min","Genre":"Drama","Director":"Frank Darabont","Writer":"Stephen King, Frank Darabont","Actors":"Tim Robbins, Morgan Freeman, Bob Gunton","Plot":"Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.","Language":"English","Country":"United States","Awards":"Nominated for 7 Oscars. 21 wins & 43 nominations total","Poster":"https://m.media-amazon.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SX300.jpg","Ratings":[{"Source":"Internet Movie Database","Value":"9.3/10"},{"Source":"Rotten Tomatoes","Value":"91%"},{"Source":"Metacritic","Value":"81/100"}],"Metascore":"81","imdbRating":"9.3","imdbVotes":"2,559,562","imdbID":"tt0111161","Type":"movie","DVD":"21 Dec 1999","BoxOffice":"$28,767,189","Production":"N/A","Website":"N/A","Response":"True"},
    {"Title":"The Godfather","Year":"1972","Rated":"R","Released":"24 Mar 1972","Runtime":"175 min","Genre":"Crime, Drama","Director":"Francis Ford Coppola","Writer":"Mario Puzo, Francis Ford Coppola","Actors":"Marlon Brando, Al Pacino, James Caan","Plot":"The aging patriarch of an organized crime dynasty in postwar New York City transfers control of his clandestine empire to his reluctant youngest son.","Language":"English, Italian, Latin","Country":"United States","Awards":"Won 3 Oscars. 31 wins & 30 nominations total","Poster":"https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SX300.jpg","Ratings":[{"Source":"Internet Movie Database","Value":"9.2/10"},{"Source":"Rotten Tomatoes","Value":"97%"},{"Source":"Metacritic","Value":"100/100"}],"Metascore":"100","imdbRating":"9.2","imdbVotes":"1,765,414","imdbID":"tt0068646","Type":"movie","DVD":"11 May 2004","BoxOffice":"$136,381,073","Production":"N/A","Website":"N/A","Response":"True"},
    {"Title":"The Dark Knight","Year":"2008","Rated":"PG-13","Released":"18 Jul 2008","Runtime":"152 min","Genre":"Action, Crime, Drama","Director":"Christopher Nolan","Writer":"Jonathan Nolan, Christopher Nolan, David S. Goyer","Actors":"Christian Bale, Heath Ledger, Aaron Eckhart","Plot":"When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.","Language":"English, Mandarin","Country":"United States, United Kingdom","Awards":"Won 2 Oscars. 159 wins & 163 nominations total","Poster":"https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SX300.jpg","Ratings":[{"Source":"Internet Movie Database","Value":"9.1/10"},{"Source":"Rotten Tomatoes","Value":"94%"},{"Source":"Metacritic","Value":"84/100"}],"Metascore":"84","imdbRating":"9.1","imdbVotes":"2,528,462","imdbID":"tt0468569","Type":"movie","DVD":"09 Dec 2008","BoxOffice":"$534,987,076","Production":"N/A","Website":"N/A","Response":"True"},
]

class Movie:
    def __init__(self, title, year, released):
        # START
        pass
        # END

    def __str__(self):
        # Dodati sve podatke o filmu
        # START
        pass
        # END




movies_list = []
for movie in movies:
    # iz kolekcije rjecnika unesti podatke u objekt i svaki objekt dodajte u novu listu
    # START
    pass
    # END


for m in movies_list:
    print(m)
