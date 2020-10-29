def zad4():
    print(dir("naprzykład"))
    help("naprzykład".endswith("ok") )
#zad4()


def zad5():
   imie ="Mateusz Śliwiński"
   print(imie[::-1])


def zad6():
    lista=[1,2,3,4,5,6,7,8,9,10]
    lista2 = []

    for licznik in range(5):
        lista2.append(lista[5+licznik])

    for licznik in range(5):
        lista.pop()

    print(lista)
    print(lista2)

def zad8():
    krotka = (151270, 150044, "Andrzej", "Mateusz", "Strzeszewski", "Śliwiski")
    krotka_indeksów=krotka[0:2]
    krotka_imion=krotka[2:4]
    krotka_nazwisk=krotka[4:6]
    print(krotka_imion)
    print(krotka_indeksów)
    print(krotka_nazwisk)
    krotka_studenta1=krotka[0:1]+krotka[2:3]+krotka[4:5]
    print(krotka_studenta1)
    krotka_studenta2 = krotka[1:2] + krotka[3:4] + krotka[5:6]
    print(krotka_studenta2)
#zad8()



def zad9():
    studenci = {
        151270: (21, "andrzej@andrzejowadomena.pl", 1999, "Warszawa ul Słoneczna 11"),
        150044: (21, "mati@mati.pl", 1999, "Lubowidz ul. Zielona 6"),
        }
    print(studenci[151270])


def zad10():
    numery = [1, 2, 2, 2, 2, 3, 56]
    numery = set(numery)
    print(numery)

def zad11():
   for i in range (11):
       print(i)

def zad12():
    for i in range(100, 15, -5):
        print(i)


