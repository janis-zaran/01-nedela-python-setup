"""
3. nedēļas mājasdarbs — datu kolekciju prakse.

Šajā failā ir piemēri ar:
- sarakstiem
- vārdnīcām
- sarakstu ar vārdnīcām
"""

# --- A daļa: Saraksti ---

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.append(11)   # pievienojam elementu
removed_number = numbers.pop()  # izdzēšam pēdējo elementu


def calculate_sum_and_average(items):
    """Aprēķina saraksta summu un vidējo vērtību ar for ciklu.

    Args:
        items: Saraksts ar skaitļiem.

    Returns:
        tuple: (summa, vidējā vērtība)
    """
    total = 0
    count = 0

    for item in items:
        total += item
        count += 1

    average = total / count if count > 0 else 0
    return total, average


def get_even_numbers(items):
    """Atgriež tikai pāra skaitļus no saraksta.

    Args:
        items: Saraksts ar skaitļiem.

    Returns:
        list: Jauns saraksts ar pāra skaitļiem.
    """
    evens = []
    for item in items:
        if item % 2 == 0:
            evens.append(item)
    return evens


# --- B daļa: Vārdnīcas ---

students = {
    "Anna": 85,
    "Jānis": 72,
    "Līga": 95
}

students["Pēteris"] = 88      # pievienojam jaunu studentu
students["Jānis"] = 75        # mainām esošu atzīmi


def get_best_student(student_grades):
    """Atrod studentu ar augstāko atzīmi.

    Args:
        student_grades: Vārdnīca formātā {vārds: atzīme}.

    Returns:
        tuple: (studenta_vārds, atzīme)
    """
    best_name = None
    best_grade = -1

    for name, grade in student_grades.items():
        if grade > best_grade:
            best_name = name
            best_grade = grade

    return best_name, best_grade


# --- C daļa: Kombinācija ---

student_list = [
    {"name": "Anna", "grade": 85},
    {"name": "Jānis", "grade": 75},
    {"name": "Līga", "grade": 95},
    {"name": "Pēteris", "grade": 88},
]


def filter_students_by_grade(items, min_grade=80):
    """Filtrē studentus ar atzīmi, kas ir lielāka vai vienāda par min_grade.

    Args:
        items: Saraksts ar vārdnīcām, kur katra vārdnīca satur studenta datus.
        min_grade: Minimālā atzīme.

    Returns:
        list: Filtrēts studentu saraksts.
    """
    filtered = []
    for student in items:
        if student["grade"] >= min_grade:
            filtered.append(student)
    return filtered


if __name__ == "__main__":
    print("--- Saraksti ---")
    total, average = calculate_sum_and_average(numbers)
    print(f"Summa: {total}, Vidējais: {average}")
    print(f"Pāra skaitļi: {get_even_numbers(numbers)}")
    print(f"Pirmie 3: {numbers[:3]}")
    print(f"Pēdējie 2: {numbers[-2:]}")
    print(f"Katrs otrais elements: {numbers[::2]}")
    print(f"Izdzēstais elements ar pop(): {removed_number}")

    print("\n--- Vārdnīcas ---")
    for name, grade in students.items():
        print(f"{name}: {grade}")

    best_name, best_grade = get_best_student(students)
    print(f"Labākais students: {best_name} ({best_grade})")

    print("\n--- Studenti ar atzīmi >= 80 ---")
    filtered_students = filter_students_by_grade(student_list, 80)
    for index, student in enumerate(filtered_students, start=1):
        print(f"{index}. {student['name']} — {student['grade']}")