movie = {
    "Title":"The Shawshank Redemption",
    "Year":"1994",
    "Rated":"R",
    "Released":"14 Oct 1994",
    "Runtime":"142 min",
    "Genre":"Drama",
    "Director":"Frank Darabont",
    "Writer":"Stephen King, Frank Darabont",
    "Actors":"Tim Robbins, Morgan Freeman, Bob Gunton",
    "Plot":"Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
    "Language":"English",
    "Country":"United States",
    "Awards":"Nominated for 7 Oscars. 21 wins & 43 nominations total",
    "Poster":"https://m.media-amazon.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SX300.jpg",
    "Ratings":[
        {
            "Source":"Internet Movie Database",
            "Value":"9.3/10"
         },
        {
            "Source":"Rotten Tomatoes",
            "Value":"91%"
        },
        {
            "Source":"Metacritic",
            "Value":"81/100"
        }
    ],
    "Metascore":"81",
    "imdbRating":"9.3",
    "imdbVotes":"2,559,562",
    "imdbID":"tt0111161",
    "Type":"movie",
    "DVD":"21 Dec 1999",
    "BoxOffice":"$28,767,189",
    "Production":"N/A",
    "Website":"N/A",
    "Response":"True"
}

# Film [naziv_filma] je zaradio [iznos] [valuta].

naziv_filma = movie["Title"]
iznos = str(movie["BoxOffice"][1 : ])
iznos = iznos.replace(',', '')
# valuta = movie["BoxOffice"]
valuta = movie["BoxOffice"][0]
# valuta_simbol = valuta[0]
# valuta = valuta[0]
#        "$28,767,189"[0]
#        "$28,767,189"                $
#        "28,767,189"
#        "28767189"

print(f'Film "{naziv_filma}" je zaradio {iznos} {valuta}.')
