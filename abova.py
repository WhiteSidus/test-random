import random

random_pole = []

points = int(0)
live = 2

def nove_kolo():
    global random_pole
    random_pole.append(random.randint(5, 15))

for i in range(random.randint(1,15)):
    print(f"Počet životu - {live}")
    print(f"Počet bodu - {points}")

    print(f"\nKolo čislo {i+1}")
    print("Pokud chcete skončit, napište kód nouzového zastavení - 228")
    
    for j in range(random.randint(1, 15)):
        nove_kolo()

    print(random_pole)

    odpoved = int(input(f"Napíšte prosim delku pole v kole {i+1}: "))

    if odpoved == len(random_pole):
        print("Hezky. Máš +1 bod")
        points = points+1

    elif odpoved == 228:
        print(f"Jsi celkově měl {points} bodu")
        break

    else:
        print("Blbečku, maš -1 život")
        live = live-1

        if live == 0:
            print("GG, jsi udělal vše co mohl! :_( ")
            print(f"Jsi celkově měl {points} bodu")
            break