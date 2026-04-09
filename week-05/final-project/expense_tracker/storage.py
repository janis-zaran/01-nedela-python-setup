import json
import os

EXPENSES_FILE = "expenses.json"


def load_expenses():
    """Ielādē izdevumus no expenses.json faila."""
    if not os.path.exists(EXPENSES_FILE):
        return []

    try:
        with open(EXPENSES_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_expenses(expenses):
    """Saglabā izdevumus expenses.json failā."""
    with open(EXPENSES_FILE, "w", encoding="utf-8") as file:
        json.dump(expenses, file, ensure_ascii=False, indent=4)