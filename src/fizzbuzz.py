import sys

# 1. PĀRBAUDĀM ARGUMENTUS
# sys.argv[0] ir faila nosaukums, sys.argv[1] ir pirmais arguments (skaitlis N)
if len(sys.argv) < 2:
    print("Kļūda: Lūdzu, norādi skaitli N! (Piemēram: python fizzbuzz.py 15)")
    sys.exit()

try:
    n = int(sys.argv[1])
except ValueError:
    print(f"Kļūda: '{sys.argv[1]}' nav derīgs vesels skaitlis!")
    sys.exit()

# 2. FIZZBUZZ LOĢIKA
rezultati = []

for i in range(1, n + 1):
    izvade = ""
    
    # Pārbaudām dalāmību (atlikums % ir 0)
    if i % 3 == 0:
        izvade += "Fizz"
    if i % 5 == 0:
        izvade += "Buzz"
    if i % 7 == 0:          # Bonuss: Jazz
        izvade += "Jazz"
        
    # Ja neviens no nosacījumiem neizpildījās, izmantojam pašu skaitli
    if izvade == "":
        izvade = str(i)
        
    rezultati.append(izvade)

# 3. IZVADE (savienojam sarakstu vienā rindā ar komatiem)
print(", ".join(rezultati))
