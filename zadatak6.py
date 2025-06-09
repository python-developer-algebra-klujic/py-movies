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
import json


def write_movies_to_json(filename, movies):
    """Serializes the list of movie dictionaries into a JSON file.

    Args:
        filename (str): Name of the file to write to.
        movies (list[dict]): List of movies, each represented as dict with
            keys: "title", "director", "year".

    The JSON file must be pretty–printed (indent‑level 4) and encoded as UTF‑8.
    """

    # START SOLUTION

    # END SOLUTION


def read_movies_from_json(filename):
    """Čita JSON datoteku i vraća listu filmova."""

    """Funkcija read_movies_from_json(filename) otvara zadanu JSON datoteku i pretvara njezin sadržaj
    u Python listu rječnika filmova. Datoteka se mora čitati s UTF-8 kodiranjem,
    a rezultat vratiti kao povratna vrijednost.
    Dopušteno je koristiti samo standardni modul json, bez vanjskih biblioteka."""
    # START SOLUTION


    # END SOLUTION


def main():
    sample = [
        {"title": "Blade Runner", "director": "Ridley Scott", "year": 1982},
        {"title": "Spirited Away", "director": "Hayao Miyazaki", "year": 2001},
    ]
    fname = "movies.json"
    write_movies_to_json(fname, sample)
    restored = read_movies_from_json(fname)
    assert restored == sample
    print("All tests passed.")


if __name__ == "__main__":
    main()