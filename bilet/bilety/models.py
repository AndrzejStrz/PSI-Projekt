from django.db import models


class Uzytkownik(models.Model):
    id_Uzytkownik = models.IntegerField(null=False)
    Imie = models.CharField(max_length=45)
    Nazwisko = models.CharField(max_length=45)
    Login = models.CharField(max_length=45)
    Haslo = models.CharField(max_length=45)
    Mail = models.CharField(max_length=45)


class Opcje_Biletu(models.Model):
    id_Opcje_Biletu = models.IntegerField(null=False)
    Cena = models.FloatField(null=False)
    Nazwa_Biletu = models.CharField(max_length=45)


class Podroze(models.Model):
    id_Podroze = models.IntegerField(null=False)
    Trasa = models.CharField(max_length=45)
    Data = models.DateField(null=False)


class Pociag(models.Model):
    id_pociag = models.IntegerField(null=False)
    Nazwa = models.CharField(max_length=45)


class Wagon(models.Model):
    id_Wagon = models.IntegerField(null=False)
    Ilosc_Miejsc = models.IntegerField(null=False)
    Pociag_id_Pociag = models.ForeignKey(Pociag, on_delete=models.CASCADE, null=False)


class Miejsce(models.Model):
    id_Miejsce = models.IntegerField(null=False)
    Numer_Miejsca = models.IntegerField(null=False)
    Numer_Biletu = models.IntegerField(null=False)
    Wagon_id_Wagon = models.ForeignKey(Wagon, on_delete=models.CASCADE, null=False)


class Bilet(models.Model):
    id_Bilet = models.IntegerField(null=False)
    Pociag_id_Pociag=models.ForeignKey(Pociag, on_delete=models.CASCADE, null=False)
    Uzytkownik_id_Uzytkownik = models.ForeignKey(Uzytkownik, on_delete=models.CASCADE, null=False)
    Opcje_Biletu_id_Opcje_Biletu = models.ForeignKey(Opcje_Biletu, on_delete=models.CASCADE, null=False)
    Podroz_id_Podroz= models.ForeignKey(Podroze, on_delete=models.CASCADE, null=False)


