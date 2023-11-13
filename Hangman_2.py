import os
import random

# Funkcija za čišćenje ekrana
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Funkcija za prikaz glavnog izbornika
def prikazi_glavni_izbornik():
    clear_screen()
    print("=== Hangman  ===")
    print("1. Jedan igrač")
    print("2. Dva igrača")
    print("3. Hall of Fame")
    print("4. Izlaz")
    odabir = input("Odaberite opciju: ")
    if odabir == "1":
        igraj_jednog_igraca()
    elif odabir == "2":
        igraj_dva_igraca()
    elif odabir == "3":
        prikazi_hall_of_fame()
    elif odabir == "4":
        exit()
    else:
        print("Pogrešan odabir. Molimo pokušajte ponovno.")
        prikazi_glavni_izbornik()

# Funkcija za unos imena igrača
def unesi_imena_igraca():
    clear_screen()
    ime1 = input("Unesite ime prvog igrača: ")
    ime2 = input("Unesite ime drugog igrača: ")
    return ime1, ime2

# Funkcija za učitavanje pojma iz trajne memorije
def ucitaj_pojam():
    with open("pojmovi.txt", "r")as datoteka:
        pojmovi = datoteka.read().splitlines()
    pojam = random.choice(pojmovi)
    return pojam.lower()


# Funkcija za prikaz vješala i neuspjelih pokušaja
def prikazi_vjesala(neuspjeli_pokusaji):
    vjesala = [
        """
           _____
          |     |
                |
                |
                |
                |
        """,
        """
           _____
          |     |
          O     |
                |
                |
                |
        """,
        """
           _____
          |     |
          O     |
          |     |
                |
                |
        """,
        """
           _____
          |     |
          O     |
         /|     |
                |
                |
        """,
        """
           _____
          |     |
          O     |
         /|\    |
                |
                |
        """,
        """
           _____
          |     |
          O     |
         /|\    |
         /      |
                |
        """,
        """
           _____
          |     |
          O     |
         /|\    |
         / \    |
                |
        """
    ]
    print(vjesala[neuspjeli_pokusaji])



def pohrani_rezultat(ime, bodovi):
    with open("rezultati_2.txt", "a") as datoteka:
        datoteka.write(f"{ime}:{bodovi}\n")

# Funkcija za prikaz stanja igre
def prikazi_stanje_igre(pojmovi, slova_pogodjena, neuspjeli_pokusaji):
    print("\nStanje igre:")
    for slovo in pojmovi:
        if slovo in slova_pogodjena:
            print(slovo, end=" ")
        else:
            print("_", end=" ")
    print("\n")
    print("Neuspjeli pokušaji:", neuspjeli_pokusaji)
    print("Pogodjena slova:", ", ".join(slova_pogodjena))
    print("\n")

# Funkcija za igru jednog igrača
def igraj_jednog_igraca():
    ime = input("Unesite svoje ime: ")
    pojmovi = ucitaj_pojam()
    pobjeda = False
    neuspjeli_pokusaji = 0
    slova_pogodjena = []
    while neuspjeli_pokusaji < len(pojmovi) and not pobjeda:
        clear_screen()
        prikazi_vjesala(neuspjeli_pokusaji)
        for slovo in pojmovi:
            if slovo in slova_pogodjena:
                print(slovo, end=" ")
            else:
                print("_", end=" ")
        print()
        prijedlog = input("Pogodite slovo ili cijeli pojam: ")
        if len(prijedlog) == 1:
            if prijedlog in pojmovi:
                slova_pogodjena.append(prijedlog)
            else:
                neuspjeli_pokusaji += 1
        elif prijedlog == pojmovi:
            pobjeda = True
    if pobjeda:
        print(f"Igrač {ime} je pobjednik!")
        pohrani_rezultat(ime, len(pojmovi)- neuspjeli_pokusaji)
    else:
        print("Niste pogodili pojam.")
    input("Pritisnite Enter za povratak na glavni izbornik.")
    prikazi_glavni_izbornik()

# Funkcija za igru dva igrača
def igraj_dva_igraca():
    ime1, ime2 = unesi_imena_igraca()
    print(f"Igrač 1: {ime1}")
    print(f"Igrač 2: {ime2}")

    # Igrač 1
    pojmovi1 = ucitaj_pojam()
    pobjeda1 = False
    neuspjeli_pokusaji1 = 0
    slova_pogodjena1 = []

    # Igrač 2
    pojmovi2 = ucitaj_pojam()
    pobjeda2 = False
    neuspjeli_pokusaji2 = 0
    slova_pogodjena2 = []

    trenutni_igrac = 1

    while (neuspjeli_pokusaji1 < len(pojmovi1) and not pobjeda1) or (neuspjeli_pokusaji2 < len(pojmovi2) and not pobjeda2):
        if trenutni_igrac == 1:
            print(f"Na redu je Igrač {ime1}.")
            prikazi_vjesala(neuspjeli_pokusaji1)  # Dodajte ovdje poziv funkcije prikazi_vjesala
            prikazi_stanje_igre(pojmovi1, slova_pogodjena1, neuspjeli_pokusaji1)
            prijedlog = input("Unesite slovo ili cijeli pojam: ")
            if len(prijedlog) == 1:
                if prijedlog in pojmovi1:
                    slova_pogodjena1.append(prijedlog)
                else:
                    neuspjeli_pokusaji1 += 1
            else:
                if prijedlog == "".join(pojmovi1):
                    pobjeda1 = True
                    break
                else:
                    neuspjeli_pokusaji1 += 1

            # Provjera pobjede nakon unosa prijedloga
            if pobjeda1:
                print(f"Igrac {ime1} je pobjednik!")
                pohrani_rezultat(ime1,len(pojmovi1) - neuspjeli_pokusaji1)
            trenutni_igrac = 2
        else:
            print(f"Na redu je Igrač {ime2}.")
            prikazi_vjesala(neuspjeli_pokusaji2)  # Dodajte ovdje poziv funkcije prikazi_vjesala
            prikazi_stanje_igre(pojmovi2, slova_pogodjena2, neuspjeli_pokusaji2)
            prijedlog = input("Unesite slovo ili cijeli pojam: ")
            if len(prijedlog) == 1:
                if prijedlog in pojmovi2:
                    slova_pogodjena2.append(prijedlog)
                else:
                    neuspjeli_pokusaji2 += 1
            else:
                if prijedlog == pojmovi2:
                    pobjeda2 = True
                    break
                else:
                    neuspjeli_pokusaji2 += 1

            if pobjeda2:
                print(f"Igrac {ime2} je pobjendik")
                pohrani_rezultat(ime2, len(pojmovi2)- neuspjeli_pokusaji2)

            trenutni_igrac = 1

    if pobjeda1:
        print(f"Igrač {ime1} je pobjednik!")
        pohrani_rezultat(ime1, len(pojmovi1) - neuspjeli_pokusaji1)
    elif pobjeda2:
        print(f"Igrač {ime2} je pobjednik!")
        pohrani_rezultat(ime2, len(pojmovi2) - neuspjeli_pokusaji2)
    else:
        print("Niste pogodili pojmove.")

    input("Pritisnite Enter za povratak na glavni izbornik.")
    prikazi_glavni_izbornik()



# Funkcija za prikaz Hall of Fame
def prikazi_hall_of_fame():
    clear_screen()
    print("=== Hall of Fame ===")
    with open("rezultati_2.txt", "r")as file:
        rezultati = file.readlines()

        if len(rezultati) == 0:
            print("Nema dostupnih rezultata.")
        else:
            print("Rang\tIme\t\tRezultat")
            print("------------------")
            for i, rezultat in enumerate(rezultati, start=1):
                rezultat = rezultat.strip()
                ime, bodovi = rezultat.split(":")
                print(f"{i}\t{ime}\t\t{bodovi}")

        input("Pritisnite Enter za povratak na glavni izbornik.")
        prikazi_glavni_izbornik()

# Glavni program
prikazi_glavni_izbornik()


