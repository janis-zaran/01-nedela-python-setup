import json  # Importē json moduli darbam ar JSON failiem
import os  # Importē os moduli, lai pārbaudītu, vai faili eksistē

SHOPPING_FILE = "shopping.json"  # Faila nosaukums iepirkumu sarakstam
PRICES_FILE = "prices.json"  # Faila nosaukums cenu datubāzei


def load_json(filename, default_value):  # Universāla funkcija JSON faila ielādei
    """Ielādē JSON datus no faila."""
    if not os.path.exists(filename):  # Pārbauda, vai fails eksistē
        return default_value  # Ja neeksistē, atgriež noklusējuma vērtību

    try:  # Mēģina atvērt un nolasīt failu
        with open(filename, "r", encoding="utf-8") as file:  # Atver failu lasīšanai
            return json.load(file)  # Nolasa un atgriež JSON saturu
    except (json.JSONDecodeError, OSError):  # Ja rodas kļūda faila lasīšanā
        return default_value  # Atgriež noklusējuma vērtību


def save_json(filename, data):  # Universāla funkcija JSON faila saglabāšanai
    """Saglabā JSON datus failā."""
    with open(filename, "w", encoding="utf-8") as file:  # Atver failu rakstīšanai
        json.dump(data, file, ensure_ascii=False, indent=4)  # Saglabā datus JSON formātā


def load_items():  # Funkcija ielādē iepirkumu sarakstu
    """Ielādē iepirkumu sarakstu."""
    return load_json(SHOPPING_FILE, [])  # Ielādē shopping.json vai atgriež tukšu sarakstu


def save_items(items):  # Funkcija saglabā iepirkumu sarakstu
    """Saglabā iepirkumu sarakstu."""
    save_json(SHOPPING_FILE, items)  # Saglabā sarakstu shopping.json failā


def load_prices():  # Funkcija ielādē cenu datubāzi
    """Ielādē cenu datubāzi."""
    return load_json(PRICES_FILE, {})  # Ielādē prices.json vai atgriež tukšu vārdnīcu


def save_prices(prices):  # Funkcija saglabā cenu datubāzi
    """Saglabā cenu datubāzi."""
    save_json(PRICES_FILE, prices)  # Saglabā datus prices.json failā


def get_price_for_product(name):  # Funkcija atrod iepriekš saglabātu cenu produktam
    """Atrod iepriekš saglabātu cenu produktam."""
    prices = load_prices()  # Ielādē visas cenas no faila
    return prices.get(name.lower())  # Meklē produktu pēc nosaukuma mazajiem burtiem


def remember_price(name, price):  # Funkcija saglabā produkta cenu cenu datubāzē
    """Saglabā produkta cenu cenu datubāzē."""
    prices = load_prices()  # Ielādē esošo cenu datubāzi
    prices[name.lower()] = price  # Saglabā vai atjauno cenu konkrētajam produktam
    save_prices(prices)  # Saglabā atjaunoto cenu datubāzi


def add_item(name, quantity, price_per_unit):  # Funkcija pievieno produktu iepirkumu sarakstam
    """Pievieno produktu iepirkumu sarakstam."""
    items = load_items()  # Ielādē esošos produktus

    item = {  # Izveido viena produkta ierakstu
        "name": name,  # Produkta nosaukums
        "quantity": quantity,  # Produkta daudzums
        "price_per_unit": price_per_unit  # Cena par vienību
    }  # Beidzas vārdnīca

    items.append(item)  # Pievieno produktu sarakstam
    save_items(items)  # Saglabā atjaunoto iepirkumu sarakstu
    remember_price(name, price_per_unit)  # Saglabā cenu arī cenu datubāzē


def calculate_item_total(item):  # Funkcija aprēķina vienas pozīcijas summu
    """Aprēķina vienas pozīcijas summu."""
    return item["quantity"] * item["price_per_unit"]  # Daudzums reizināts ar cenu


def calculate_total():  # Funkcija aprēķina visu iepirkumu kopējo summu
    """Aprēķina kopējo summu."""
    items = load_items()  # Ielādē visus produktus
    total = 0  # Izveido mainīgo kopējai summai

    for item in items:  # Iziet cauri visiem produktiem
        total += calculate_item_total(item)  # Pieskaita katras pozīcijas summu

    return total  # Atgriež kopējo summu


def clear_items():  # Funkcija notīra iepirkumu sarakstu
    """Notīra iepirkumu sarakstu."""
    save_items([])  # Saglabā tukšu sarakstu shopping.json failā


def print_items(items):  # Funkcija izvada visus produktus
    """Izdrukā iepirkumu sarakstu."""
    if not items:  # Pārbauda, vai saraksts nav tukšs
        print("Saraksts ir tukšs.")  # Izvada ziņu, ja nav produktu
        return  # Beidz funkciju

    for index, item in enumerate(items, start=1):  # Iziet cauri produktiem ar numerāciju
        total = calculate_item_total(item)  # Aprēķina vienas pozīcijas summu
        print(
            f"{index}. {item['name']} | daudzums: {item['quantity']} | "
            f"cena/gab: {item['price_per_unit']:.2f} EUR | "
            f"summa: {total:.2f} EUR"
        )  # Izvada vienu produktu ar visu informāciju


def ask_float(prompt):  # Funkcija prasa lietotājam ievadīt skaitli
    """Prasa lietotājam ievadīt skaitli."""
    while True:  # Turpina jautāt, līdz ievade ir pareiza
        value = input(prompt).strip()  # Nolasa lietotāja ievadi
        try:  # Mēģina pārveidot uz skaitli
            return float(value)  # Atgriež float vērtību
        except ValueError:  # Ja pārveidošana neizdodas
            print("Lūdzu ievadi derīgu skaitli.")  # Izvada kļūdas ziņu


def add_item_interactive():  # Funkcija interaktīvi pievieno produktu
    """Interaktīvi pievieno produktu."""
    name = input("Produkta nosaukums: ").strip()  # Prasa produkta nosaukumu
    if not name:  # Pārbauda, vai nosaukums nav tukšs
        print("Nosaukums nedrīkst būt tukšs.")  # Izvada kļūdas ziņu
        return  # Beidz funkciju

    quantity = ask_float("Daudzums: ")  # Prasa daudzumu
    if quantity <= 0:  # Pārbauda, vai daudzums ir lielāks par 0
        print("Daudzumam jābūt lielākam par 0.")  # Izvada kļūdas ziņu
        return  # Beidz funkciju

    known_price = get_price_for_product(name)  # Meklē, vai šim produktam jau ir saglabāta cena

    if known_price is not None:  # Ja cena jau ir zināma
        print(f"Iepriekšējā cena produktam '{name}': {known_price:.2f} EUR")  # Parāda iepriekšējo cenu
        use_old_price = input("Vai izmantot šo cenu? (j/n): ").strip().lower()  # Prasa, vai lietot veco cenu

        if use_old_price == "j":  # Ja lietotājs izvēlas izmantot veco cenu
            price_per_unit = known_price  # Izmanto iepriekš saglabāto cenu
        else:  # Ja lietotājs negrib veco cenu
            price_per_unit = ask_float("Jaunā cena par vienību: ")  # Prasa jaunu cenu
    else:  # Ja cena iepriekš nav saglabāta
        price_per_unit = ask_float("Cena par vienību: ")  # Prasa ievadīt cenu

    if price_per_unit < 0:  # Pārbauda, vai cena nav negatīva
        print("Cena nedrīkst būt negatīva.")  # Izvada kļūdas ziņu
        return  # Beidz funkciju

    add_item(name, quantity, price_per_unit)  # Pievieno produktu sarakstam
    print("Produkts pievienots.")  # Apstiprina pievienošanu


def main():  # Galvenā funkcija ar izvēlni
    while True:  # Bezgalīgs cikls, līdz lietotājs izvēlas iziet
        print("\n--- Iepirkumu saraksts (3. solis) ---")  # Izvada virsrakstu
        print("1. Pievienot produktu")  # Izvada 1. opciju
        print("2. Apskatīt sarakstu")  # Izvada 2. opciju
        print("3. Aprēķināt kopējo summu")  # Izvada 3. opciju
        print("4. Notīrīt sarakstu")  # Izvada 4. opciju
        print("5. Apskatīt cenu datubāzi")  # Izvada 5. opciju
        print("6. Iziet")  # Izvada 6. opciju

        choice = input("Izvēlies darbību: ").strip()  # Nolasa lietotāja izvēli

        if choice == "1":  # Ja lietotājs izvēlas pievienot produktu
            add_item_interactive()  # Palaiž interaktīvo pievienošanu

        elif choice == "2":  # Ja lietotājs izvēlas apskatīt sarakstu
            print("\n--- Saraksts ---")  # Izvada sadaļas nosaukumu
            print_items(load_items())  # Ielādē un izvada iepirkumu sarakstu

        elif choice == "3":  # Ja lietotājs izvēlas kopējo summu
            print(f"Kopējā summa: {calculate_total():.2f} EUR")  # Izvada kopējo summu

        elif choice == "4":  # Ja lietotājs izvēlas notīrīt sarakstu
            clear_items()  # Notīra sarakstu
            print("Saraksts notīrīts.")  # Apstiprina notīrīšanu

        elif choice == "5":  # Ja lietotājs izvēlas apskatīt cenu datubāzi
            prices = load_prices()  # Ielādē cenu datubāzi

            if not prices:  # Pārbauda, vai cenu datubāze nav tukša
                print("Cenu datubāze ir tukša.")  # Izvada ziņu
            else:  # Ja cenu datubāzē ir dati
                print("\n--- Cenu datubāze ---")  # Izvada sadaļas nosaukumu
                for name, price in prices.items():  # Iziet cauri visām cenām
                    print(f"{name}: {price:.2f} EUR")  # Izvada vienu produktu un cenu

        elif choice == "6":  # Ja lietotājs izvēlas iziet
            print("Programma beidzas.")  # Izvada beigu ziņu
            break  # Pārtrauc ciklu

        else:  # Ja ievade nav pareiza
            print("Nepareiza izvēle.")  # Izvada kļūdas ziņu


if __name__ == "__main__":  # Pārbauda, vai fails palaists tieši
    main()  # Izsauc galveno funkciju