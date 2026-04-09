from datetime import date, datetime
from storage import load_expenses, save_expenses
from logic import filter_by_month, sum_total, sum_by_category, get_available_months
from export import export_to_csv

CATEGORIES = [
    "Ēdiens",
    "Transports",
    "Izklaide",
    "Komunālie maksājumi",
    "Veselība",
    "Iepirkšanās",
    "Cits",
]


def show_menu():
    """Parāda izvēlni un atgriež lietotāja izvēli."""
    print("\n" + "=" * 50)
    print("Izdevumu izsekotājs")
    print("=" * 50)
    print("1) Pievienot izdevumu")
    print("2) Parādīt izdevumus")
    print("3) Filtrēt pēc mēneša")
    print("4) Kopsavilkums pa kategorijām")
    print("5) Dzēst izdevumu")
    print("6) Eksportēt CSV")
    print("7) Iziet")
    return input("Izvēlies darbību (1-7): ").strip()


def is_valid_date(text):
    """Pārbauda, vai datums ir derīgs YYYY-MM-DD formātā."""
    try:
        datetime.strptime(text, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def ask_date():
    """Prasa lietotājam datumu vai izmanto šodienas datumu."""
    default_date = date.today().strftime("%Y-%m-%d")
    user_input = input(f"Datums (YYYY-MM-DD) [{default_date}]: ").strip()

    if user_input == "":
        return default_date

    if is_valid_date(user_input):
        return user_input

    print("Nepareizs datuma formāts. Izmanto YYYY-MM-DD.")
    return None


def ask_category():
    """Prasa lietotājam izvēlēties kategoriju."""
    print("Kategorija:")
    for index, category in enumerate(CATEGORIES, start=1):
        print(f"  {index}) {category}")

    choice = input(f"Izvēlies (1-{len(CATEGORIES)}): ").strip()

    try:
        number = int(choice)
        if 1 <= number <= len(CATEGORIES):
            return CATEGORIES[number - 1]
    except ValueError:
        pass

    print("Nepareiza kategorijas izvēle.")
    return None


def ask_amount():
    """Prasa lietotājam ievadīt derīgu summu."""
    user_input = input("Summa (EUR): ").strip()

    try:
        amount = float(user_input)
        if amount < 0:
            raise ValueError
        return round(amount, 2)
    except ValueError:
        print("Nepareiza summa.")
        return None


def show_expenses_list(expenses):
    """Parāda izdevumu sarakstu tabulas veidā."""
    if not expenses:
        print("Nav izdevumu.")
        return

    print(f"{'Nr.':<4} {'Datums':<12} {'Summa':>10} {'Kategorija':<22} Apraksts")
    print("-" * 80)

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index:<4} "
            f"{expense['date']:<12} "
            f"{expense['amount']:>8.2f} EUR  "
            f"{expense['category']:<22} "
            f"{expense['description']}"
        )

    print("-" * 80)
    print(f"Kopā: {sum_total(expenses):.2f} EUR ({len(expenses)} ieraksti)")


def add_expense_ui(expenses):
    """Interaktīvi pievieno jaunu izdevumu."""
    expense_date = ask_date()
    if expense_date is None:
        return

    category = ask_category()
    if category is None:
        return

    amount = ask_amount()
    if amount is None:
        return

    description = input("Apraksts: ").strip()
    if description == "":
        description = "Bez apraksta"

    expense = {
        "date": expense_date,
        "amount": amount,
        "category": category,
        "description": description,
    }

    expenses.append(expense)
    save_expenses(expenses)

    print(f"✓ Pievienots: {expense_date} | {category} | {amount:.2f} EUR | {description}")


def show_expenses_ui(expenses):
    """Parāda visus izdevumus."""
    show_expenses_list(expenses)


def filter_by_month_ui(expenses):
    """Parāda izdevumus izvēlētajam mēnesim."""
    months = get_available_months(expenses)

    if not months:
        print("Nav pieejamu izdevumu filtrēšanai.")
        return

    print("Pieejamie mēneši:")
    for index, month_text in enumerate(months, start=1):
        print(f"  {index}) {month_text}")

    choice = input("Izvēlies mēnesi: ").strip()

    try:
        number = int(choice)
        if not (1 <= number <= len(months)):
            raise ValueError
    except ValueError:
        print("Nepareiza mēneša izvēle.")
        return

    selected_month = months[number - 1]
    year_text, month_text = selected_month.split("-")
    filtered = filter_by_month(expenses, int(year_text), int(month_text))

    print(f"\n{selected_month} izdevumi:")
    show_expenses_list(filtered)


def show_summary_ui(expenses):
    """Parāda summas pa kategorijām."""
    if not expenses:
        print("Nav izdevumu kopsavilkumam.")
        return

    totals = sum_by_category(expenses)

    print("Kopsavilkums pa kategorijām:")
    print("-" * 40)

    for category, total in totals.items():
        print(f"{category:<22} {total:>10.2f} EUR")

    print("-" * 40)
    print(f"KOPĀ: {sum_total(expenses):.2f} EUR")


def delete_expense_ui(expenses):
    """Dzēš izdevumu pēc numura."""
    if not expenses:
        print("Nav izdevumu, ko dzēst.")
        return

    print("Izdevumi:")
    show_expenses_list(expenses)

    choice = input("Kuru dzēst? (numurs vai 0 lai atceltu): ").strip()

    try:
        number = int(choice)
    except ValueError:
        print("Nepareiza ievade.")
        return

    if number == 0:
        print("Dzēšana atcelta.")
        return

    if not (1 <= number <= len(expenses)):
        print("Nepareizs ieraksta numurs.")
        return

    deleted = expenses.pop(number - 1)
    save_expenses(expenses)

    print(
        f"✓ Dzēsts: {deleted['date']} | {deleted['amount']:.2f} EUR | "
        f"{deleted['category']} | {deleted['description']}"
    )


def export_csv_ui(expenses):
    """Eksportē izdevumus CSV failā."""
    if not expenses:
        print("Nav izdevumu eksportēšanai.")
        return

    filename = input("Faila nosaukums [izdevumi.csv]: ").strip()
    if filename == "":
        filename = "izdevumi.csv"

    export_to_csv(expenses, filename)
    print(f"✓ Eksportēts: {len(expenses)} ieraksti -> {filename}")


def main():
    """Palaiž galveno programmas ciklu."""
    expenses = load_expenses()

    while True:
        choice = show_menu()

        if choice == "1":
            add_expense_ui(expenses)
        elif choice == "2":
            show_expenses_ui(expenses)
        elif choice == "3":
            filter_by_month_ui(expenses)
        elif choice == "4":
            show_summary_ui(expenses)
        elif choice == "5":
            delete_expense_ui(expenses)
        elif choice == "6":
            export_csv_ui(expenses)
        elif choice == "7":
            print("Uz redzēšanos!")
            break
        else:
            print("Nepareiza izvēle. Mēģini vēlreiz.")


if __name__ == "__main__":
    main()