def zad2():
    lorem_ipsum = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"
    imie = "Andrzej"
    nazwisko = "Strzeszewski"

    liczba_liter1 = 0
    liczba_liter2 = 0
    for litera in lorem_ipsum:
        if (imie[2] == litera):
            liczba_liter1 += 1
        if (nazwisko[3] == litera):
            liczba_liter2 += 1
    print('W tekście jest ' + str(liczba_liter1) + ' liter ' + str(imie[2]) + ' oraz ' + str(
        liczba_liter2) + ' liter ' + str(nazwisko[3]))

def zad3():
    tekst = "Kaczki lubią pływać"
    pi = 3.141592653589793238462643383279502884197169399375

    print('{:^33}'.format(tekst))
    print('{:06.4f}'.format(pi))
    print('{:=+5d}'.format(- 1))
    print('{:.{prec}} = {:.{prec}f}'.format('pi', 3.1415926, prec=2))
    print('{:{}{sign}{}.{}}'.format(3.1415926, '=', 10, 4, sign='+'))

def zad6():
    lista = [1,2,3,4,5,6,7,8,9,10]
    lista2 = []

    for licznik in range(5):
        lista2.append(lista[5+licznik])

    for licznik in range(5):
        lista.pop()

    print(lista)
    print(lista2)

def zad7():
    lista1 = [1, 2, 3, 4, 5]
    lista2 = [6, 7, 8, 9, 10]
    lista_połączona = []
    lista_połączona_kopia= []
    for licznik in range(10):
        if(licznik<5):
            lista_połączona.append(str(lista1[licznik]))
        else:
            lista_połączona.append(str(lista2[licznik-5]))
    for licznik in range(10):
        lista_połączona[licznik]=int(lista_połączona[licznik])

    lista_połączona = [0] + lista_połączona
    lista_połączona_kopia = lista_połączona

    for licznik in range(11):
        print(lista_połączona[10-licznik], end=" ")

def zad9():
    studenci = {
        151270: (21, "andrzej@andrzejowadomena.pl", 1999, "Warszawa ul Słoneczna 11"),
        150044: (21, "mati@mati.pl", 1999, "Grudziądz ul. Zielona 6"),
    }
    print(studenci[151270])

def zad10():
    numery = [111999111,111999111,111999111,111999112,111999113,111999188,111999100, 111999100]
    numery = set(numery)
    print(numery)

