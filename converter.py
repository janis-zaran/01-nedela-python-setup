# converter.py

# 1. KONSTANTES (Mērvienību koeficienti)
KM_TO_MI = 0.621371
KG_TO_LB = 2.20462
L_TO_GAL = 0.264172
USD_TO_EUR = 0.84235020

print("--- VIENĪBU KONVERTORS ---")
print("Izvēlies kategoriju:")
print("1) km <-> mi  2) kg <-> lb  3) L <-> gal  4) $ <-> €")

kategorija = input("> ")

print("Izvēlies virzienu: 1) No kreisās uz labo  2) No labās uz kreiso")
virziens = input("> ")

ievade = input("Ievadi vērtību: ")

# 2. PĀRBAUDĀM IEVADI UN VEICAM APRĒĶINUS
try:
    vertiba = float(ievade) # Mēģinām pārvērst ievadi par skaitli
    rezultats = 0.0
    no_vieniba = ""
    uz_vieniba = ""

    # Kilometri / Jūdzes
    if kategorija == "1":
        if virziens == "1":
            rezultats = vertiba * KM_TO_MI
            no_vieniba, uz_vieniba = "km", "mi"
        else:
            rezultats = vertiba / KM_TO_MI
            no_vieniba, uz_vieniba = "mi", "km"

    # Kilogrami / Mārciņas
    elif kategorija == "2":
        if virziens == "1":
            rezultats = vertiba * KG_TO_LB
            no_vieniba, uz_vieniba = "kg", "lb"
        else:
            rezultats = vertiba / KG_TO_LB
            no_vieniba, uz_vieniba = "lb", "kg"

    # Litri / Galoni
    elif kategorija == "3":
        if virziens == "1":
            rezultats = vertiba * L_TO_GAL
            no_vieniba, uz_vieniba = "L", "gal"
        else:
            rezultats = vertiba / L_TO_GAL
            no_vieniba, uz_vieniba = "gal", "L"

    # Dolāri / Eiro
    elif kategorija == "4":
        if virziens == "1":
            rezultats = vertiba * USD_TO_EUR
            no_vieniba, uz_vieniba = "$", "€"
        else:
            rezultats = vertiba / USD_TO_EUR
            no_vieniba, uz_vieniba = "€", "$"
    
    else:
        print("Nepareiza kategorijas izvēle!")
        exit() # Beidzam programmu, ja izvēle nav 1-4

    # 3. REZULTĀTA IZVADE (ar f-string un 2 zīmēm aiz komata)
    print(f"\nREVALUĀCIJA: {vertiba:.2f} {no_vieniba} = {rezultats:.2f} {uz_vieniba}")

except ValueError:
    # Šis izpildās, ja lietotājs ievada tekstu, nevis skaitli
    print(f"KĻŪDA: '{ievade}' nav derīgs skaitlis!")
