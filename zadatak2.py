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

def group_books_by_letter(books):
    """Grupira naslove knjiga prema prvom slovu (bez obzira na velika i mala slova)."""

    """Funkcija group_books_by_letter(books) prima listu naslova knjiga i vraća rječnik gdje je ključ prvo veliko slovo,
    a vrijednost lista naslova koji tim slovom započinju. Redoslijed naslova unutar pojedine liste
    mora ostati isti kao u ulaznoj listi. Prazne stringove zanemari i ne koristi vanjske biblioteke."""
    # START SOLUTION


    # END SOLUTION


def main():
    sample = ["Dune", "Dracula", "Foundation", "Frankenstein", "1984", "It"]
    grouped = group_books_by_letter(sample)
    assert grouped["D"] == ["Dune", "Dracula"]
    assert grouped["F"] == ["Foundation", "Frankenstein"]
    assert grouped["I"] == ["It"]
    assert "1" not in grouped  # Titles starting with digits are skipped
    print("All tests passed.")


if __name__ == "__main__":
    main()