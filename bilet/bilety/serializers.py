from rest_framework import serializers
from .models import Uzytkownik, Opcje_Biletu, Podroze, Pociag, Wagon, Miejsce, Bilet
from .views import *
from .models import Uzytkownik as Mail

class UzytkownikSerializer(serializers.ModelSerializer):

    Imie = serializers.SlugRelatedField(many=False, read_only=True,
                                          slug_field="Maciek")

    class Meta:
        model = Uzytkownik
        fields = ['id_Uzytkownik','Imie','Nazwisko','Login','Haslo','Mail']

    def Create(self, Validate_data):
        return UzytkownikSerializer(**Validate_data)

    def Update(self, instance, validate_data):
        instance.id_Uzytkownik = validate_data.get('id_Uzytkownik', instance.id_Uzytkownik)
        instance.Imie = validate_data.get('Imie', instance.imie)
        instance.Nazwiwsko = validate_data.get('Nazwisko', instance.nazwisko)
        instance.Login = validate_data.get('Login', instance.login)
        instance.Haslo = validate_data.get('Haslo', instance.Haslo)
        instance.Mail = validate_data.get('Mail', instance.Mail)
        instance.save()
        return instance

class Opcje_BiletuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opcje_Biletu
        fields = ['id_Opcje_Biletu', 'Cena', 'Nazwa_Biletu']

    def Create(self, Validate_data):
        return Opcje_BiletuSerializer(**Validate_data)

    def update(self, instance, validate_date):
        instance.id_Opcje_Biletu = validate_date('id_Opcje_Biletu', instance.id_Opcje_Biletu)
        instance.Cena = validate_date('Cena', instance.Cena)
        instance.Nazwa_Biletu = validate_date('Nazwa_Biletu', instance.Nazwa_Biletu)
        instance.save()
        return instance

class PodrozeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podroze
        fields = ['id_Podroze','Trasa','Data']

    def Create(self, Validate_data):
        return PodrozeSerializer(**Validate_data)

    def Update(self, instance, validate_date):
        instance.id_Podroze = validate_date('id_Podroze', instance.id_Podroze)
        instance.Trasa = validate_date('Trasa', instance.Trasa)
        instance.Data = validate_date('Data', instance.Data)
        instance.save()
        return instance

class PociagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pociag
        fields = ['id_pociag','Nazwa']

    def Create(self, Validate_data):
        return PociagSerializer(**Validate_data)

    def Update(self, instance, validate_date):
        instance.id_Pociag = validate_date('id_Pociag', instance.id_Pociag)
        instance.Nazwa = validate_date('Nazwa', instance.Nazwa)
        instance.save()
        return instance

class WagonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wagon
        fields = ['id_Wagon', 'Ilosc_Miejsc', 'Pociag_id_Pociag']

    def Create(self, Validate_data):
        return WagonSerializer(**Validate_data)

    def Update(self, instance, validate_date):
        instance.id_Wagon = validate_date('id_Wagon', instance.id_Wagon)
        instance.Ilosc_Miejsc = validate_date('Ilosc_Miejsc', instance.Ilosc_Miejsc)
        instance.Pociag_id_Pociag = validate_date('Pociag_id_Pociag', instance.Pociag_id_Pociag)
        instance.save()
        return instance

class MiejsceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Miejsce
        fields = ['id_Miejsce','Numer_Miejsca','Wagon_id_Wagon']
    def Create(self, Validate_data):
        return MiejsceSerializer(**Validate_data)

    def Update(self, instance, validate_date):
        instance.id_Miejsce = validate_date('id_Miejsce', instance.id_Miejsce)
        instance.Numer_Miejsc = validate_date('Numer_Miejsc', instance.Numer_Miejsc)
        instance.Wagon_id_Wagon = validate_date('Wagon_id_Wagon', instance.Wagon_id_Wagon)
        instance.save()
        return instance

class BiletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bilet
        fields = ['id_Bilet', 'Pociag_id_Pociag', 'Uzytkownik_id_Uzytkownik', 'Opcje_Biletu_id_Opcje_Biletu',
                'Podroz_id_Podroz']

    def Create(self, Validate_data):
        return BiletSerializer(**Validate_data)

    def Update(self, instance, validate_date):
        instance.id_Bilet = validate_date('id_Bilet', instance.id_Bilet)
        instance.Pociag_id_Pociag = validate_date('Pociag_id_Pociag', instance.Pociag_id_Pociag)
        instance.Uzytkownik_id_Uzytkownik = validate_date('Uzytkownik_id_Uzytkownik',
                                                          instance.Uzytkownik_id_Uzytkownik)
        instance.Opcje_Biletu_id_Opcje_Biletu = validate_date('Opcje_Biletu_id_Opcje_Biletu',
                                                              instance.Opcje_Biletu_id_Opcje_Biletu)
        instance.Podroz_id_Podroz = validate_date('Podroz_id_Podroz', instance.Podroz_id_Podroz)
        instance.save()
        return instance
