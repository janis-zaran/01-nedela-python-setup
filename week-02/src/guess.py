import random

# Ārējais cikls: Ļauj spēlēt spēli vēlreiz
while True:
    slepenais = random.randint(1, 100)
    meginajumi = 0
    max_meginajumi = 10
    uzminets = False

    print("\n--- SKAITĻU MINĒŠANAS SPĒLE (1-100) ---")
    print(f"Tev ir {max_meginajumi} mēģinājumi!")

    # Iekšējais cikls: Pašas minēšanas process
    while meginajumi < max_meginajumi:
        ievade = input(f"Mēģinājums {meginajumi + 1}/{max_meginajumi}. Tavs minējums: ")

        # 1. Pārbaudām, vai ievadīts skaitlis
        try:
            minejums = int(ievade)
        except ValueError:
            print("Kļūda: Lūdzu, ievadi veselu skaitli!")
            continue # Atgriežas cikla sākumā, nepieskaitot mēģinājumu

        meginajumi += 1

        # 2. Pārbaudām minējumu
        if minejums < slepenais:
            print("Par mazu!")
        elif minejums > slepenais:
            print("Par lielu!")
        else:
            uzminets = True
            break # Uzminēts! Lecam ārā no minēšanas cikla

    # 3. Spēles beigu paziņojums
    if uzminets:
        print(f"APSVEICU! Uzminēji skaitli {slepenais} ar {meginajumi}. mēģinājumu.")
    else:
        print(f"ZAUDĒJI! Mēģinājumi beidzās. Pareizais skaitlis bija {slepenais}.")

    # 4. Vai spēlēt vēlreiz?
    velreiz = input("\nVai vēlies spēlēt vēlreiz? (j/n): ").lower()
    if velreiz != 'j':
        print("Paldies par spēli! Atā!")
        break # Pārtrauc ārējo ciklu un beidz programmu
