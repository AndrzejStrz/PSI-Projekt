
#zad1
def zad1(a_list, b_list):
    return [i for i in a_list if i % 2 == 0] + [i for i in b_list if i % 2 == 0]

#print(zad1([0,1,2,3], [5,6,7,8]))


def zad2(txt):
    slownik = {
        'length': len(txt),
        'letters': [char for char in txt],
        'big_letters': txt.upper(),
        'small_letters': txt.lower()
    }
    return slownik

#slownik = zad2("Aha byczku +1")
#print(slownik['letters'])

def zad3(letter, text):
    return text.replace(letter, "")

#print(zad3('a',"kokaspaniel"))

def zad4(type, temp):
    if type == 'K':
        return 273.15 + temp
    elif type == 'R':
        return (temp + 273.15) * 1.8
    elif type == 'F':
        return (temp * 1.8) + 32
    else:
        return "Nieprawidłowy typ"

print(zad4('K',20))

#zad5
class kalkulator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def dodaj(self, a, b):
        return a + b

    def odejmij(self, a, b):
        return a - b

    def podziel(self, a, b):
        return a / b

    def pomnoz(self, a, b):
        return a * b


# kalkulator=kalkulator(5,3)
# print(kalkulator.dodaj(5,3))
# print(kalkulator.odejmij(5,3))
# print(kalkulator.podziel(5,3))
# print(kalkulator.pomnoz(5,3))

# zadanie 6
class ScienceKalkulator(kalkulator):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def potegowanie(self, a):
        return a * a


# ScienceKalkulator =ScienceKalkulator(5,3)
# print(ScienceKalkulator.potegowanie(5))
# print(ScienceKalkulator.dodaj(5,3))

# zad7

def odwrot():
    tekst = input()
    return tekst[::-1]


# print(odwrot())

# zad8

class FileManager:
    def __init__(self, file_name):
        self.file_name = file_name


    def FileRead(self,file_name):

        file_name = open('plik.txt')
        dane=file_name.read()
        return print(dane)

    def update_file(self,file_name):
        plik = open(self.file_name + ".txt", "a")
        plik.write('text_data')
        plik.close()




FileManager = FileManager('plik.txt')
print(FileManager.FileRead('plik.txt'))


