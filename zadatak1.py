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

def unique_movies(titles):
    """Grupira naslove knjiga prema prvom slovu (nije osjetljivo na velika/mala slova)."""


    """Funkcija group_books_by_letter(books) prima listu naslova knjiga i vraća listu s jednstvenim,
    nazivima filmova. Redoslijed naslova unutar pojedine liste mora ostati isti kao u ulaznoj listi.
    Prazne stringove zanemari i ne koristi vanjske biblioteke."""
    # START SOLUTION


    # END SOLUTION


def main():
    assert unique_movies(["Alien", "Alien", "Aliens"]) == ["Alien", "Aliens"]
    assert unique_movies([1, 2, 3]) == []
    assert unique_movies([]) == []
    assert unique_movies(["Inception", "Memento", "Inception", "Interstellar"]) == ["Inception", "Memento", "Interstellar"]
    print("All tests passed.")


if __name__ == "__main__":
    main()