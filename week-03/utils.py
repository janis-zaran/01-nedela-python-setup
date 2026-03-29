"""
Utilītu bibliotēka ar atkārtoti lietojamām funkcijām.
"""

from typing import Any


def capitalize(text: str) -> str:
    """Pārvērš virknes pirmo burtu par lielo.

    Args:
        text: Ievades teksts.

    Returns:
        str: Teksts ar lielo pirmo burtu.

    Example:
        >>> capitalize("hello")
        'Hello'
    """
    if not isinstance(text, str):
        raise ValueError("text jābūt virknei")
    if text == "":
        return ""
    return text[0].upper() + text[1:]


def truncate(text: str, max_len: int = 20, suffix: str = "...") -> str:
    """Saīsina tekstu līdz noteiktam garumam un pievieno suffix.

    Args:
        text: Ievades teksts.
        max_len: Maksimālais garums.
        suffix: Pievienojamais galotnes teksts.

    Returns:
        str: Saīsināts teksts.

    Example:
        >>> truncate("Python programmēšana ir interesanta", 10)
        'Python ...'
    """
    if not isinstance(text, str):
        raise ValueError("text jābūt virknei")
    if not isinstance(max_len, int) or max_len < 0:
        raise ValueError("max_len jābūt nenegatīvam veselam skaitlim")
    if not isinstance(suffix, str):
        raise ValueError("suffix jābūt virknei")

    if len(text) <= max_len:
        return text
    if max_len <= len(suffix):
        return suffix[:max_len]
    return text[: max_len - len(suffix)] + suffix


def count_words(text: str) -> int:
    """Saskaita vārdus tekstā.

    Args:
        text: Ievades teksts.

    Returns:
        int: Vārdu skaits.

    Example:
        >>> count_words("Python ir foršs")
        3
    """
    if not isinstance(text, str):
        raise ValueError("text jābūt virknei")

    words = text.split()
    count = 0
    for _ in words:
        count += 1
    return count


def clamp(num: float, low: float, high: float) -> float:
    """Ierobežo skaitli dotajā diapazonā.

    Args:
        num: Skaitlis, ko ierobežot.
        low: Minimālā robeža.
        high: Maksimālā robeža.

    Returns:
        float: Ierobežotā vērtība.

    Example:
        >>> clamp(15, 0, 10)
        10
    """
    if low > high:
        raise ValueError("low nedrīkst būt lielāks par high")
    if num < low:
        return low
    if num > high:
        return high
    return num


def is_prime(num: int) -> bool:
    """Pārbauda, vai skaitlis ir pirmskaitlis.

    Args:
        num: Pārbaudāmais skaitlis.

    Returns:
        bool: True, ja ir pirmskaitlis, citādi False.

    Example:
        >>> is_prime(7)
        True
    """
    if not isinstance(num, int):
        raise ValueError("num jābūt veselam skaitlim")

    if num < 2:
        return False

    divisor = 2
    while divisor * divisor <= num:
        if num % divisor == 0:
            return False
        divisor += 1
    return True


def factorial(n: int) -> int:
    """Aprēķina skaitļa faktoriālu.

    Args:
        n: Nenegatīvs vesels skaitlis.

    Returns:
        int: Faktoriāla vērtība.

    Example:
        >>> factorial(5)
        120
    """
    if not isinstance(n, int):
        raise ValueError("n jābūt veselam skaitlim")
    if n < 0:
        raise ValueError("n jābūt >= 0")

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def total(numbers: list[float]) -> float:
    """Aprēķina saraksta elementu summu ar for ciklu.

    Args:
        numbers: Saraksts ar skaitļiem.

    Returns:
        float: Elementu summa.

    Example:
        >>> total([1, 2, 3])
        6
    """
    if not isinstance(numbers, list):
        raise ValueError("numbers jābūt sarakstam")

    result = 0
    for number in numbers:
        if not isinstance(number, (int, float)):
            raise ValueError("Visiem elementiem jābūt skaitļiem")
        result += number
    return result


def average(numbers: list[float], default: float = 0) -> float:
    """Aprēķina saraksta vidējo aritmētisko.

    Args:
        numbers: Saraksts ar skaitļiem.
        default: Vērtība, ko atgriezt tukšam sarakstam.

    Returns:
        float: Vidējā vērtība.

    Example:
        >>> average([2, 4, 6])
        4.0
    """
    if not isinstance(numbers, list):
        raise ValueError("numbers jābūt sarakstam")
    if len(numbers) == 0:
        return default

    count = 0
    for number in numbers:
        if not isinstance(number, (int, float)):
            raise ValueError("Visiem elementiem jābūt skaitļiem")
        count += 1

    return total(numbers) / count


def first_non_empty(*args: Any) -> Any:
    """Atgriež pirmo vērtību, kas nav tukša.

    Args:
        *args: Mainīgs argumentu skaits.

    Returns:
        Any: Pirmā netukšā vērtība vai None.

    Example:
        >>> first_non_empty("", None, "Python")
        'Python'
    """
    for value in args:
        if value not in ("", None, [], {}, ()):
            return value
    return None


if __name__ == "__main__":
    print("--- utils.py demonstrācija ---")
    print(capitalize("hello"))
    print(truncate("Python programmēšana ir interesanta", 15))
    print(count_words("Python valoda ir jaudīga"))
    print(clamp(15, 0, 10))
    print(is_prime(11))
    print(factorial(5))
    print(total([1, 2, 3, 4]))
    print(average([1, 2, 3, 4]))
    print(first_non_empty("", None, "atrasts"))