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

def write_books_to_csv(filename, books):
    """Writes a list of book dictionaries to a CSV file.

    CSV columns: title,author,pages
    """

    # START SOLUTION

    # END SOLUTION


def average_pages_from_csv(filename):
    """Čita CSV datoteku i vraća aritmetičku sredinu broja stranica."""

    """Funkcija average_pages_from_csv(filename) prima naziv CSV datoteke sa stupcem 'pages'
    i računa aritmetičku sredinu broja stranica svih knjiga. 
    Prvu liniju (zaglavlje) treba preskočiti, a prazne ili neispravne retke ignorirati.
    Ako nema valjanih podataka, funkcija treba vratiti 0."""
    # START SOLUTION


    # END SOLUTION


def main():
    books = [
        {"title": "Dune", "author": "Frank Herbert", "pages": 604},
        {"title": "1984", "author": "George Orwell", "pages": 328},
        {"title": "The Hobbit", "author": "J. R. R. Tolkien", "pages": 310},
    ]
    fname = "books.csv"
    write_books_to_csv(fname, books)
    assert round(average_pages_from_csv(fname), 2) == round((604 + 328 + 310) / 3, 2)
    print("All tests passed.")


if __name__ == "__main__":
    main()