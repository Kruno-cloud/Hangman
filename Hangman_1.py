import random
import os

pojam = ""
pogodjena_slova = []
neuspjesni_pokusaji = []


def glavni_izbornik():
    print("----- HANGMAN -----")
    print("1. Ulaz u igru za jednog igrača")
    print("2. Ulaz u igru za dva igrača")
    print("3. Pregled tablice najboljih igrača")
    print("4. Izlaz iz aplikacije")


def unesi_imena_igraca(broj_igraca):
    imena = []
    for i in range(broj_igraca):
        ime = input("Unesite ime igrača {}: ".format(i + 1))
        imena.append(ime)
    return imena


def ucitaj_pojam_iz_memorije():
    pojmovi = ["banana", "jabuka", "kivi", "breskva"]
    return random.choice(pojmovi)


def prikazi_pojam(pojam, pogodjena_slova):
    prikaz = ""
    for slovo in pojam:
        if slovo in pogodjena_slova:
            prikaz += slovo + " "
        else:
            prikaz += "_ "
    print(prikaz)

def prikazi_stanje(pojam, pogodjena_slova):
    prikaz = ""
    for slovo in pojam:
        if slovo in pogodjena_slova:
            prikaz += slovo + " "
        else:
            prikaz += "_ "
    print(prikaz)



def odabir_poteza(igrac, pojam, pogodjena_slova, neuspjesni_pokusaji):
    print("\nNa redu je igrač", igrac)
    print("Pojam:")
    prikazi_stanje(pojam, pogodjena_slova)
    print("Neuspješni pokušaji:", neuspjesni_pokusaji)

    izbor = input("Unesite voće koje nema [š,č,ć,đ,ž] te odaberite što želite napraviti? (s - predložiti slovo, p - pogoditi pojam): ")
    return izbor


def predlozi_slovo():
    slovo = input("Unesite slovo: ")
    return slovo


def pogodi_pojam():
    poj = input("Pogodite pojam: ")
    return poj


def igra_za_jednog():
    print("IGRA ZA JEDNOG IGRAČA")
    imena = unesi_imena_igraca(1)
    igrac = imena[0]
    pojam = ucitaj_pojam_iz_memorije()
    pogodjena_slova = []
    neuspjesni_pokusaji = []
    broj_bodova = 0
    while True:
        potez = odabir_poteza(igrac, pojam, pogodjena_slova, neuspjesni_pokusaji)

        if potez == "s":
            slovo = predlozi_slovo()
            if slovo in pojam:
                pogodjena_slova.append(slovo)
                print("Točno! Pogodili ste slovo.")
            else:
                neuspjesni_pokusaji.append(slovo)
                print("Netočno! To slovo se ne nalazi u pojmu.")
                if len(neuspjesni_pokusaji) == 6:
                    print("Izgubili ste! Svi dijelovi tijela su iscrtani na vješalu.")
                    break
        elif potez == "p":
            poj = pogodi_pojam()
            if poj == pojam:
                print("Čestitamo,", igrac, "je pobjednik!")
                break
            else:
                neuspjesni_pokusaji.append(poj)
                print("Netočno! Pogriješili ste pojam.")
                if len(neuspjesni_pokusaji) == 6:
                    print("Izgubili ste! Svi dijelovi tijela su iscrtani na vješalu.")
                    break
        else:
            print("Pogrešan unos! Molimo pokušajte ponovno.")

    pohrani_rezultat(igrac, broj_bodova)


def igra_za_dva():
    print("IGRA ZA DVA IGRAČA")
    imena = unesi_imena_igraca(2)
    igrac1, igrac2 = imena
    pojam = ucitaj_pojam_iz_memorije()
    pogodjena_slova = []
    neuspjesni_pokusaji = []
    broj_bodova_igrac1 = 0
    broj_bodova_igrac2 = 0
    trenutni_igrac = igrac1  # Postavljamo početnog igrača na igrac1

    while True:
        while True:
            potez = odabir_poteza(trenutni_igrac, pojam, pogodjena_slova, neuspjesni_pokusaji)

            if potez == "s":
                slovo = predlozi_slovo()
                if slovo in pojam:
                    pogodjena_slova.append(slovo)
                    print("Točno! Pogodili ste slovo.")
                else:
                    neuspjesni_pokusaji.append(slovo)
                    print("Netočno! To slovo se ne nalazi u pojmu.")
                    if len(neuspjesni_pokusaji) == 6:
                        print("Izgubio je igrač", trenutni_igrac, "! Svi dijelovi tijela su iscrtani na vješalu.")
                        break
            elif potez == "p":
                poj = pogodi_pojam()
                if poj == pojam:
                    print("Čestitamo,", trenutni_igrac, "je pobjednik!")
                    break
                else:
                    neuspjesni_pokusaji.append(poj)
                    print("Netočno! Pogriješili ste pojam.")
                    if len(neuspjesni_pokusaji) == 6:
                        print("Izgubio je igrač", trenutni_igrac, "! Svi dijelovi tijela su iscrtani na vješalu.")
                        break
            else:
                print("Pogrešan unos! Molimo pokušajte ponovno.")

        if len(neuspjesni_pokusaji) == 6:
            break

        # Prebacivanje na sljedećeg igrača
        if trenutni_igrac == igrac1:
            trenutni_igrac = igrac2
        else:
            trenutni_igrac = igrac1

        # Prikaz trenutnog rezultata
        print("Rezultat:")
        print(igrac1, ":", broj_bodova_igrac1, "bodova")
        print(igrac2, ":", broj_bodova_igrac2, "bodova")

        # Provjera je li igra završila
        if broj_bodova_igrac1 == 3:
            print("Čestitamo,", igrac1, "je ukupni pobjednik!")
            pohrani_rezultat(igrac1, broj_bodova_igrac1)
            break
        elif broj_bodova_igrac2 == 3:
            print("Čestitamo,", igrac2, "je ukupni pobjednik!")
            pohrani_rezultat(igrac2, broj_bodova_igrac2)
            break
        else:
            print("Nova runda! Pojam za pogadjanje je:", pojam)

def pohrani_rezultat(ime, bodovi):
    with open("rezultati_1.txt", "a") as datoteka:
        datoteka.write(f"{ime}:{bodovi}\n")

def ucitaj_rezultate():
    if os.path.exists("rezultati_1.txt"):
        with open("rezultati_1.txt", "r") as datoteka:
            rezultati = []
            for linija in datoteka:
                ime, bodovi = linija.strip().split(":")
                rezultati.append((ime, int(bodovi)))
    else:
        rezultati = []
    return rezultati

def prikazi_rezultate():
    rezultati = ucitaj_rezultate()
    if not rezultati:
        print("Trenutno nema rezultata.")
    else:
        print("\t\tHANGMAN - TABLICA NAJBOLJIH IGRAČA")
        print("-------------------------------")
        print("\t\tIME\t\tBODOVI")
        print("-------------------------------")
        for ime, bodovi in rezultati:
            print(f"\t\t{ime}\t\t{bodovi}")
        print("-------------------------------")

def main():
    while True:
        glavni_izbornik()
        odabir = input("Odaberite opciju: ")

        if odabir == "1":
            igra_za_jednog()
        elif odabir == "2":
            igra_za_dva()
        elif odabir == "3":
            prikazi_rezultate()
        elif odabir == "4":
            print("Hvala što ste igrali HANGMAN!")
            break
        else:
            print("Pogrešan unos! Molimo pokušajte ponovno.")

if __name__ == "__main__":
    main()
