from datetime import datetime


def sum_total(expenses):
    """Aprēķina visu izdevumu kopējo summu."""
    total = 0

    for expense in expenses:
        total += expense["amount"]

    return round(total, 2)


def filter_by_month(expenses, year, month):
    """Atgriež tikai tos izdevumus, kas ir norādītajā gadā un mēnesī."""
    result = []

    for expense in expenses:
        expense_date = datetime.strptime(expense["date"], "%Y-%m-%d")

        if expense_date.year == year and expense_date.month == month:
            result.append(expense)

    return result


def sum_by_category(expenses):
    """Atgriež vārdnīcu ar kopsummām pa kategorijām."""
    totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        totals[category] = totals.get(category, 0) + amount

    rounded_totals = {}

    for category, total in totals.items():
        rounded_totals[category] = round(total, 2)

    return rounded_totals


def get_available_months(expenses):
    """Atgriež unikālo mēnešu sarakstu formātā YYYY-MM."""
    months = []

    for expense in expenses:
        expense_date = datetime.strptime(expense["date"], "%Y-%m-%d")
        month_text = expense_date.strftime("%Y-%m")

        if month_text not in months:
            months.append(month_text)

    months.sort()
    return months