import json  # Importē json moduli darbam ar JSON failiem
import os  # Importē os moduli, lai pārbaudītu, vai fails eksistē

SHOPPING_FILE = "shopping.json"  # Norāda faila nosaukumu, kur glabāsies iepirkumu dati


def load_items():  # Funkcija ielādē produktus no JSON faila
    """Ielādē iepirkumu sarakstu no JSON faila."""  # Funkcijas apraksts
    if not os.path.exists(SHOPPING_FILE):  # Pārbauda, vai shopping.json fails eksistē
        return []  # Ja fails neeksistē, atgriež tukšu sarakstu

    try:  # Mēģina atvērt un nolasīt failu
        with open(SHOPPING_FILE, "r", encoding="utf-8") as file:  # Atver failu lasīšanai
            return json.load(file)  # Nolasa JSON datus un atgriež tos kā Python sarakstu
    except (json.JSONDecodeError, OSError):  # Ja rodas kļūda lasīšanā vai JSON bojāts
        return []  # Atgriež tukšu sarakstu


def save_items(items):  # Funkcija saglabā produktus JSON failā
    """Saglabā iepirkumu sarakstu JSON failā."""  # Funkcijas apraksts
    with open(SHOPPING_FILE, "w", encoding="utf-8") as file:  # Atver failu rakstīšanai
        json.dump(items, file, ensure_ascii=False, indent=4)  # Saglabā datus JSON formātā


def add_item(name, price):  # Funkcija pievieno vienu produktu sarakstam
    """Pievieno produktu sarakstam."""  # Funkcijas apraksts
    items = load_items()  # Ielādē jau esošos produktus no faila

    item = {  # Izveido vārdnīcu vienam produktam
        "name": name,  # Saglabā produkta nosaukumu
        "price": price  # Saglabā produkta cenu
    }  # Beidzas vārdnīca

    items.append(item)  # Pievieno jauno produktu sarakstam
    save_items(items)  # Saglabā atjaunoto sarakstu failā


def list_items():  # Funkcija atgriež visus produktus
    """Atgriež visus produktus."""  # Funkcijas apraksts
    return load_items()  # Ielādē un atgriež visus produktus


def calculate_total():  # Funkcija aprēķina kopējo summu
    """Aprēķina kopējo summu."""  # Funkcijas apraksts
    items = load_items()  # Ielādē visus produktus
    total = 0  # Izveido mainīgo kopējai summai

    for item in items:  # Iziet cauri katram produktam
        total += item["price"]  # Pieskaita produkta cenu kopējai summai

    return total  # Atgriež kopējo summu


def clear_items():  # Funkcija notīra visu sarakstu
    """Notīra iepirkumu sarakstu."""  # Funkcijas apraksts
    save_items([])  # Saglabā tukšu sarakstu, tādējādi notīrot failu


def print_items(items):  # Funkcija izvada produktus ekrānā
    """Izdrukā produktu sarakstu."""  # Funkcijas apraksts
    if not items:  # Pārbauda, vai saraksts ir tukšs
        print("Saraksts ir tukšs.")  # Izvada ziņu, ja nav neviena produkta
        return  # Beidz funkcijas darbību

    for index, item in enumerate(items, start=1):  # Iziet cauri produktiem ar numerāciju no 1
        print(f"{index}. {item['name']} - {item['price']:.2f} EUR")  # Izvada vienu produktu


def main():  # Galvenā funkcija, kas vada programmas izvēlni
    while True:  # Bezgalīgs cikls, lai programma darbotos līdz lietotājs izvēlas iziet
        print("\n--- Iepirkumu saraksts (1. solis) ---")  # Izvada virsrakstu
        print("1. Pievienot produktu")  # Izvada 1. izvēlni
        print("2. Apskatīt sarakstu")  # Izvada 2. izvēlni
        print("3. Aprēķināt summu")  # Izvada 3. izvēlni
        print("4. Notīrīt sarakstu")  # Izvada 4. izvēlni
        print("5. Iziet")  # Izvada 5. izvēlni

        choice = input("Izvēlies darbību: ").strip()  # Nolasa lietotāja izvēli

        if choice == "1":  # Ja lietotājs izvēlas pievienot produktu
            name = input("Produkta nosaukums: ").strip()  # Prasa produkta nosaukumu
            price_text = input("Cena: ").strip()  # Prasa produkta cenu kā tekstu

            try:  # Mēģina pārveidot ievadīto cenu uz skaitli
                price = float(price_text)  # Pārveido tekstu par float skaitli
                if price < 0:  # Pārbauda, vai cena nav negatīva
                    raise ValueError  # Ja cena negatīva, izmet kļūdu
            except ValueError:  # Ja ievade nav derīga
                print("Cena jābūt nenegatīvam skaitlim.")  # Izvada kļūdas ziņu
                continue  # Atgriežas izvēlnē

            add_item(name, price)  # Pievieno produktu sarakstam
            print("Produkts pievienots.")  # Apstiprina pievienošanu

        elif choice == "2":  # Ja lietotājs izvēlas apskatīt sarakstu
            print("\n--- Saraksts ---")  # Izvada sadaļas nosaukumu
            print_items(list_items())  # Ielādē un izvada visus produktus

        elif choice == "3":  # Ja lietotājs izvēlas aprēķināt summu
            print(f"Kopējā summa: {calculate_total():.2f} EUR")  # Izvada kopējo summu

        elif choice == "4":  # Ja lietotājs izvēlas notīrīt sarakstu
            clear_items()  # Notīra visus produktus
            print("Saraksts notīrīts.")  # Apstiprina notīrīšanu

        elif choice == "5":  # Ja lietotājs izvēlas iziet
            print("Programma beidzas.")  # Izvada beigu ziņu
            break  # Pārtrauc ciklu

        else:  # Ja ievadīta nepareiza izvēle
            print("Nepareiza izvēle.")  # Izvada kļūdas ziņu


if __name__ == "__main__":  # Pārbauda, vai fails tiek palaists tieši
    main()  # Izsauc galveno funkciju