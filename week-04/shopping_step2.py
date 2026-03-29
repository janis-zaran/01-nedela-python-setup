import json  # Importē json moduli darbam ar JSON failiem
import os  # Importē os moduli, lai pārbaudītu, vai fails eksistē

SHOPPING_FILE = "shopping.json"  # Norāda JSON failu, kur glabāsies iepirkumu dati


def load_items():  # Funkcija ielādē produktus no JSON faila
    """Ielādē iepirkumu sarakstu."""
    if not os.path.exists(SHOPPING_FILE):  # Pārbauda, vai fails eksistē
        return []  # Ja neeksistē, atgriež tukšu sarakstu

    try:  # Mēģina atvērt un nolasīt failu
        with open(SHOPPING_FILE, "r", encoding="utf-8") as file:  # Atver failu lasīšanai
            return json.load(file)  # Nolasa un atgriež datus
    except (json.JSONDecodeError, OSError):  # Ja rodas kļūda faila nolasīšanā
        return []  # Atgriež tukšu sarakstu


def save_items(items):  # Funkcija saglabā produktus JSON failā
    """Saglabā iepirkumu sarakstu."""
    with open(SHOPPING_FILE, "w", encoding="utf-8") as file:  # Atver failu rakstīšanai
        json.dump(items, file, ensure_ascii=False, indent=4)  # Saglabā datus JSON formātā


def add_item(name, quantity, price_per_unit):  # Funkcija pievieno produktu ar daudzumu un cenu
    """Pievieno produktu ar daudzumu un cenu par vienību."""
    items = load_items()  # Ielādē esošos produktus

    item = {  # Izveido viena produkta vārdnīcu
        "name": name,  # Produkta nosaukums
        "quantity": quantity,  # Produkta daudzums
        "price_per_unit": price_per_unit  # Cena par vienību
    }  # Beidzas vārdnīca

    items.append(item)  # Pievieno produktu sarakstam
    save_items(items)  # Saglabā atjaunoto sarakstu failā


def calculate_item_total(item):  # Funkcija aprēķina vienas preces kopējo summu
    """Aprēķina vienas pozīcijas summu."""
    return item["quantity"] * item["price_per_unit"]  # Daudzums reizināts ar cenu par vienību


def calculate_total():  # Funkcija aprēķina visu produktu kopējo summu
    """Aprēķina visu produktu kopējo summu."""
    items = load_items()  # Ielādē visus produktus
    total = 0  # Izveido mainīgo kopējai summai

    for item in items:  # Iziet cauri visiem produktiem
        total += calculate_item_total(item)  # Pieskaita katras pozīcijas summu

    return total  # Atgriež kopējo summu


def clear_items():  # Funkcija notīra visu sarakstu
    """Notīra iepirkumu sarakstu."""
    save_items([])  # Saglabā tukšu sarakstu


def print_items(items):  # Funkcija izvada visus produktus
    """Izdrukā sarakstu ar paplašinātu informāciju."""
    if not items:  # Pārbauda, vai saraksts nav tukšs
        print("Saraksts ir tukšs.")  # Izvada ziņu, ja nav produktu
        return  # Beidz funkcijas darbību

    for index, item in enumerate(items, start=1):  # Iziet cauri produktiem ar numerāciju
        item_total = calculate_item_total(item)  # Aprēķina konkrētā produkta summu
        print(
            f"{index}. {item['name']} | daudzums: {item['quantity']} | "
            f"cena/gab: {item['price_per_unit']:.2f} EUR | "
            f"summa: {item_total:.2f} EUR"
        )  # Izvada vienu produktu ar visu informāciju


def main():  # Galvenā funkcija ar izvēlni
    while True:  # Bezgalīgs cikls, līdz lietotājs iziet
        print("\n--- Iepirkumu saraksts (2. solis) ---")  # Izvada virsrakstu
        print("1. Pievienot produktu")  # Izvada 1. opciju
        print("2. Apskatīt sarakstu")  # Izvada 2. opciju
        print("3. Aprēķināt kopējo summu")  # Izvada 3. opciju
        print("4. Notīrīt sarakstu")  # Izvada 4. opciju
        print("5. Iziet")  # Izvada 5. opciju

        choice = input("Izvēlies darbību: ").strip()  # Nolasa lietotāja izvēli

        if choice == "1":  # Ja izvēlēta produkta pievienošana
            name = input("Produkta nosaukums: ").strip()  # Prasa produkta nosaukumu
            quantity_text = input("Daudzums: ").strip()  # Prasa daudzumu
            price_text = input("Cena par vienību: ").strip()  # Prasa cenu par vienību

            try:  # Mēģina pārveidot ievadītās vērtības uz skaitļiem
                quantity = float(quantity_text)  # Pārveido daudzumu uz float
                price_per_unit = float(price_text)  # Pārveido cenu uz float

                if quantity <= 0 or price_per_unit < 0:  # Pārbauda, vai vērtības ir derīgas
                    raise ValueError  # Ja nederīgas, izmet kļūdu
            except ValueError:  # Ja ievade nav pareiza
                print("Daudzumam jābūt > 0, cenai jābūt >= 0.")  # Izvada kļūdas ziņu
                continue  # Atgriežas izvēlnē

            add_item(name, quantity, price_per_unit)  # Pievieno produktu sarakstam
            print("Produkts pievienots.")  # Apstiprina pievienošanu

        elif choice == "2":  # Ja izvēlēta saraksta apskatīšana
            print("\n--- Saraksts ---")  # Izvada sadaļas nosaukumu
            print_items(load_items())  # Ielādē un izvada produktus

        elif choice == "3":  # Ja izvēlēts aprēķināt kopējo summu
            print(f"Kopējā summa: {calculate_total():.2f} EUR")  # Izvada kopējo summu

        elif choice == "4":  # Ja izvēlēts notīrīt sarakstu
            clear_items()  # Notīra sarakstu
            print("Saraksts notīrīts.")  # Apstiprina notīrīšanu

        elif choice == "5":  # Ja izvēlēts iziet
            print("Programma beidzas.")  # Izvada beigu ziņu
            break  # Pārtrauc ciklu

        else:  # Ja izvēle nav pareiza
            print("Nepareiza izvēle.")  # Izvada kļūdas ziņu


if __name__ == "__main__":  # Pārbauda, vai fails palaists tieši
    main()  # Izsauc galveno funkciju