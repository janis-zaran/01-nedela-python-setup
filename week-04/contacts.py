import json  # Importē json moduli, lai varētu lasīt un rakstīt JSON failus
import os  # Importē os moduli, lai pārbaudītu, vai fails eksistē

CONTACTS_FILE = "contacts.json"  # Norāda faila nosaukumu, kur glabāsies kontakti


def load_contacts():  # Funkcija, kas ielādē kontaktus no JSON faila
    """Ielādē kontaktus no JSON faila."""  # Funkcijas apraksts
    if not os.path.exists(CONTACTS_FILE):  # Pārbauda, vai contacts.json fails eksistē
        return []  # Ja fails neeksistē, atgriež tukšu sarakstu

    try:  # Mēģina izpildīt faila lasīšanu
        with open(CONTACTS_FILE, "r", encoding="utf-8") as file:  # Atver failu lasīšanas režīmā
            return json.load(file)  # Nolasa JSON saturu un atgriež to kā Python sarakstu
    except (json.JSONDecodeError, OSError):  # Ja fails ir bojāts vai rodas cita kļūda
        return []  # Atgriež tukšu sarakstu


def save_contacts(contacts):  # Funkcija, kas saglabā kontaktus JSON failā
    """Saglabā kontaktus JSON failā."""  # Funkcijas apraksts
    with open(CONTACTS_FILE, "w", encoding="utf-8") as file:  # Atver failu rakstīšanas režīmā
        json.dump(contacts, file, ensure_ascii=False, indent=4)  # Saglabā sarakstu JSON formātā


def add_contact(name, phone, email):  # Funkcija, kas pievieno jaunu kontaktu
    """Pievieno jaunu kontaktu."""  # Funkcijas apraksts
    contacts = load_contacts()  # Ielādē esošos kontaktus no faila

    contact = {  # Izveido jaunu vārdnīcu ar viena kontakta datiem
        "name": name,  # Saglabā kontaktpersonas vārdu
        "phone": phone,  # Saglabā kontaktpersonas telefona numuru
        "email": email  # Saglabā kontaktpersonas e-pastu
    }  # Beidzas vārdnīcas definīcija

    contacts.append(contact)  # Pievieno jauno kontaktu kontaktu sarakstam
    save_contacts(contacts)  # Saglabā atjaunināto kontaktu sarakstu failā


def list_contacts():  # Funkcija, kas atgriež visus kontaktus
    """Atgriež visus kontaktus."""  # Funkcijas apraksts
    return load_contacts()  # Ielādē un atgriež visus kontaktus


def search_contacts(query):  # Funkcija, kas meklē kontaktus pēc ievadītā teksta
    """Meklē kontaktus pēc vārda, telefona vai e-pasta."""  # Funkcijas apraksts
    contacts = load_contacts()  # Ielādē visus kontaktus
    query = query.lower()  # Pārveido meklējamo tekstu uz mazajiem burtiem
    results = []  # Izveido tukšu sarakstu rezultātiem

    for contact in contacts:  # Iziet cauri katram kontaktam sarakstā
        if (  # Pārbauda, vai meklējamais teksts ir kādā no laukiem
            query in contact["name"].lower()  # Meklē kontaktpersonas vārdā
            or query in contact["phone"].lower()  # Meklē telefona numurā
            or query in contact["email"].lower()  # Meklē e-pastā
        ):  # Beidzas nosacījums
            results.append(contact)  # Ja atbilst, pievieno kontaktu rezultātu sarakstam

    return results  # Atgriež atrastos kontaktus


def print_contacts(contacts):  # Funkcija, kas skaisti izvada kontaktus ekrānā
    """Izvada kontaktus formatētā veidā."""  # Funkcijas apraksts
    if not contacts:  # Pārbauda, vai saraksts ir tukšs
        print("Kontakti nav atrasti.")  # Izvada ziņu, ja nav kontaktu
        return  # Beidz funkcijas darbību

    for index, contact in enumerate(contacts, start=1):  # Iziet cauri kontaktiem ar numerāciju no 1
        print(f"{index}. {contact['name']} | {contact['phone']} | {contact['email']}")  # Izvada vienu kontaktu


def main():  # Galvenā funkcija, kas vada programmas izvēlni
    while True:  # Bezgalīgs cikls, lai programma darbotos līdz lietotājs iziet
        print("\n--- Kontaktu pārvaldnieks ---")  # Izvada virsrakstu
        print("1. Pievienot kontaktu")  # Izvada 1. izvēlni
        print("2. Apskatīt visus kontaktus")  # Izvada 2. izvēlni
        print("3. Meklēt kontaktu")  # Izvada 3. izvēlni
        print("4. Iziet")  # Izvada 4. izvēlni

        choice = input("Izvēlies darbību: ").strip()  # Nolasa lietotāja izvēli un noņem liekās atstarpes

        if choice == "1":  # Pārbauda, vai lietotājs izvēlējās pievienot kontaktu
            name = input("Vārds: ").strip()  # Prasa ievadīt vārdu
            phone = input("Telefons: ").strip()  # Prasa ievadīt telefona numuru
            email = input("E-pasts: ").strip()  # Prasa ievadīt e-pastu

            if not name or not phone or not email:  # Pārbauda, vai kāds lauks nav tukšs
                print("Visi lauki ir obligāti.")  # Izvada kļūdas ziņu
                continue  # Pārlec uz nākamo cikla iterāciju

            add_contact(name, phone, email)  # Pievieno kontaktu failam
            print("Kontakts pievienots.")  # Apstiprina, ka kontakts pievienots

        elif choice == "2":  # Pārbauda, vai lietotājs izvēlējās apskatīt kontaktus
            print("\n--- Visi kontakti ---")  # Izvada sadaļas nosaukumu
            print_contacts(list_contacts())  # Ielādē un izvada visus kontaktus

        elif choice == "3":  # Pārbauda, vai lietotājs izvēlējās meklēt kontaktu
            query = input("Ievadi meklējamo tekstu: ").strip()  # Prasa ievadīt meklējamo tekstu
            print("\n--- Meklēšanas rezultāti ---")  # Izvada sadaļas nosaukumu
            print_contacts(search_contacts(query))  # Atrod un izvada meklēšanas rezultātus

        elif choice == "4":  # Pārbauda, vai lietotājs izvēlējās iziet
            print("Programma beidzas.")  # Izvada beigu ziņu
            break  # Pārtrauc ciklu un aizver programmu

        else:  # Ja ievadīta nepareiza izvēle
            print("Nepareiza izvēle.")  # Izvada kļūdas ziņu


if __name__ == "__main__":  # Pārbauda, vai fails palaists tieši, nevis importēts
    main()  # Izsauc galveno funkciju