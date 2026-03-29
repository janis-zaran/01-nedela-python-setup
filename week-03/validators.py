"""
Validācijas bibliotēka.
"""

from datetime import datetime


def is_email(text: str) -> bool:
    """Pārbauda, vai teksts izskatās pēc e-pasta adreses.

    Args:
        text: Ievades teksts.

    Returns:
        bool: True, ja teksts atbilst vienkāršai e-pasta formai.

    Example:
        >>> is_email("anna@inbox.lv")
        True
    """
    if not isinstance(text, str):
        return False

    if "@" not in text or "." not in text:
        return False

    parts = text.split("@")
    if len(parts) != 2:
        return False

    local_part, domain_part = parts
    if local_part == "" or domain_part == "":
        return False
    if "." not in domain_part:
        return False

    return True


def is_phone_number(text: str) -> bool:
    """Pārbauda, vai teksts atbilst Latvijas telefona numura formātam.

    Atļautais formāts: +371 XXXXXXXX

    Args:
        text: Ievades teksts.

    Returns:
        bool: True, ja formāts ir derīgs.

    Example:
        >>> is_phone_number("+371 26123456")
        True
    """
    if not isinstance(text, str):
        return False

    if not text.startswith("+371 "):
        return False

    digits = text[5:]
    if len(digits) != 8:
        return False

    return digits.isdigit()


def is_valid_age(age) -> bool:
    """Pārbauda, vai vecums ir vesels skaitlis diapazonā no 0 līdz 150.

    Args:
        age: Pārbaudāmā vērtība.

    Returns:
        bool: True, ja vecums ir derīgs.

    Example:
        >>> is_valid_age(25)
        True
    """
    if not isinstance(age, int):
        return False
    return 0 <= age <= 150


def is_strong_password(text: str) -> bool:
    """Pārbauda, vai parole ir pietiekami stipra.

    Nosacījumi:
    - vismaz 8 simboli
    - satur vismaz vienu burtu
    - satur vismaz vienu ciparu

    Args:
        text: Parole.

    Returns:
        bool: True, ja parole atbilst nosacījumiem.

    Example:
        >>> is_strong_password("Parole123")
        True
    """
    if not isinstance(text, str):
        return False

    if len(text) < 8:
        return False

    has_letter = False
    has_digit = False

    for char in text:
        if char.isalpha():
            has_letter = True
        if char.isdigit():
            has_digit = True

    return has_letter and has_digit


def is_valid_date(text: str) -> bool:
    """Pārbauda, vai datums ir formātā YYYY-MM-DD un ir reāls datums.

    Args:
        text: Datuma teksts.

    Returns:
        bool: True, ja datums ir derīgs.

    Example:
        >>> is_valid_date("2026-03-29")
        True
    """
    if not isinstance(text, str):
        return False

    try:
        datetime.strptime(text, "%Y-%m-%d")
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    print("--- is_email ---")
    print("is_email('anna@inbox.lv') ->", is_email("anna@inbox.lv"))
    print("is_email('anna') ->", is_email("anna"))
    print("is_email('anna@') ->", is_email("anna@"))

    print("\n--- is_phone_number ---")
    print("is_phone_number('+371 26123456') ->", is_phone_number("+371 26123456"))
    print("is_phone_number('26123456') ->", is_phone_number("26123456"))
    print("is_phone_number('+371 26123') ->", is_phone_number("+371 26123"))

    print("\n--- is_valid_age ---")
    print("is_valid_age(25) ->", is_valid_age(25))
    print("is_valid_age(0) ->", is_valid_age(0))
    print("is_valid_age(151) ->", is_valid_age(151))

    print("\n--- is_strong_password ---")
    print("is_strong_password('Parole123') ->", is_strong_password("Parole123"))
    print("is_strong_password('abcdefg') ->", is_strong_password("abcdefg"))
    print("is_strong_password('12345678') ->", is_strong_password("12345678"))

    print("\n--- is_valid_date ---")
    print("is_valid_date('2026-03-29') ->", is_valid_date("2026-03-29"))
    print("is_valid_date('2026-02-30') ->", is_valid_date("2026-02-30"))
    print("is_valid_date('29-03-2026') ->", is_valid_date("29-03-2026"))