# type_explorer.py

# 1. PIEŠĶIRAM VĒRTĪBAS MAINĪGAJIEM
vards = "Sveiki"      # str (teksts)
gadi = 25             # int (vesels skaitlis)
cena = 19.99          # float (daļskaitlis)
ir_diena = True       # bool (patiess)
tuksums = None        # None (nekas)

# 2. IZVADAM TIPUS (Pārbaudām, kas ir kas)
print("--- Mainīgo tipi ---")
print(f"'{vards}' tips ir {type(vards)}")
print(f"{gadi} tips ir {type(gadi)}")
print(f"{cena} tips ir {type(cena)}")

# 3. TRUTHY / FALSY (Kā Python saprot 'patiesību')
print("\n--- Truthy/Falsy piemēri ---")
print(bool(""))    # False - tukšs teksts skaitās "nepatiess"
print(bool(" "))   # True - atstarpe ir simbols, tātad "patiess"
print(bool(0))     # False - nulle vienmēr ir "nepatiess"

# 4. TIEŠĀ KONVERSIJA UN ROBEŽGADĪJUMI
print("\n--- Konversijas ---")

# Pārvēršam tekstu par skaitli
print(int("5") + 3)    # Rezultāts: 8

# Robežgadījums: teksts ar punktu nevar pa taisno kļūt par int
# print(int("3.14"))   # Šis izraisītu ValueError!
# Risinājums: Vispirms uz float (daļskaitli), tad uz int (veselu)
print(int(float("3.14")))  # Rezultāts: 3 (daļu vienkārši atmet)

# Konversija, kas neizdodas (ValueError)
# print(int("abc"))    # Šo nevar pārvērst, jo tie nav cipari

# 5. CITI INTERESANTI GADĪJUMI
print("\n--- Kāpēc tā notiek? ---")

# Peldošā punkta problēma
# Datori binārajā sistēmā nevar precīzi saglabāt 0.1, tāpēc rodas maza kļūda.
print(0.1 + 0.2 == 0.3)  # False (rezultāts ir 0.30000000000000004)

# Bankieru apaļošana
# Python apaļo uz tuvāko PĀRA skaitli, ja decimāldaļa ir tieši .5
print(round(2.5))  # 2
print(round(3.5))  # 4
