# eligibility.py

try:
    # 1. IEVADE
    vecums = int(input("Ievadi vecumu: "))
    
    # Pārbaudām, vai vecums nav negatīvs
    if vecums < 0:
        print("Kļūda: Vecums nevar būt negatīvs!")
        exit()

    # Funkcija, lai pārvērstu j/n par True/False
    izvele = lambda jaut: input(jaut).lower() == 'j'

    has_license = izvele("Vai ir autovadītāja apliecība? (j/n): ")
    is_student = izvele("Vai ir students? (j/n): ")
    is_veteran = izvele("Vai ir veterāns? (j/n): ")

    # 2. LOĢISKIE NOSACĪJUMI
    can_vote = vecums >= 18
    can_rent_auto = vecums >= 21 and has_license
    senior_discount = vecums >= 65 or is_veteran
    student_discount = 16 <= vecums <= 26 and is_student

    # Funkcija simbolu izvadei
    check = lambda cond: "Jā ✓" if cond else "Nē ✗"

    # 3. IZVADE AR F-STRINGS
    print("\n--- Atbilstības rezultāti ---")
    print(f"Balsošana:        {check(can_vote)}")
    print(f"Auto īre:         {check(can_rent_auto)}")
    print(f"Senioru atlaide:   {check(senior_discount)}")
    print(f"Studentu atlaide:  {check(student_discount)}")

except ValueError:
    print("Kļūda: Lūdzu, ievadiet vecumu kā skaitli!")
