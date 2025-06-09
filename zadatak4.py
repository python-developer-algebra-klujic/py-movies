"""
Owner: Algebra University, Zagreb
Address: Gradišćanska 24, 10000 Zagreb, Croatia
Web: www.algebra.hr
VAT-ID: 10750578045

Last modified: 09.06.2025.

NOTE: This script is the property of Algebra University, Zagreb. Unauthorized use is strictly prohibited.

VAŽNA NAPOMENA:
Kod izvan oznaka "# START SOLUTION" i "# END SOLUTION" ne smije se mijenjati (brisati, dodavati, mijenjati),
jer će to automatski označiti rješenje kao netočno.
"""

def split_movies_by_genre(movies):
    """Funkcija koja rastavlja listu rječnika filmova u zasebne liste po žanru."""

    """Funkcija split_movies_by_genre(movies) prima listu rječnika filmova i vraća rječnik gdje je ključ žanr,
    a vrijednost lista naslova filmova tog žanra.
    Redoslijed naslova u svakoj listi mora ostati isti kao u ulaznoj listi.
    Nije dozvoljeno koristiti vanjske biblioteke."""
    # START SOLUTION


    # END SOLUTION


def main():
    data = [
        {"title": "Alien", "genre": "Sci-Fi"},
        {"title": "Blade Runner", "genre": "Sci-Fi"},
        {"title": "The Godfather", "genre": "Crime"},
    ]
    grouped = split_movies_by_genre(data)
    assert grouped == {"Sci-Fi": ["Alien", "Blade Runner"], "Crime": ["The Godfather"]}
    print("All tests passed.")


if __name__ == "__main__":
    main()