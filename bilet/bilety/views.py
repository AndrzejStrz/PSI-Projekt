from .models import *
from .serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser
from rest_framework import generics,mixins
from django.shortcuts import render
from django.http import HttpResponse


def index (request):
    return HttpResponse("tekst")

# Create your views here.


class UzytkownikTworzy(generics.ListCreateAPIView, mixins.ListModelMixin):
    queryset = Uzytkownik.objects.all()
    serializer_class = UzytkownikSerializer

    def get(self, request):
        return self.list(request)

class UzytkownikList(APIView):

    def get(self, request, format=None):
        Uzytkownicy = Uzytkownik.objects.all()
        serializer = UzytkownikSerializer(Uzytkownicy, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UzytkownikSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    #permission_classes = [IsAuthenticated]


class UzytkownicyDetale(APIView):

        def get_object(self, pk):
            try:
                return Uzytkownik.objects.get(pk=pk)
            except Uzytkownik.DoesNotExist:
                raise Http404

        def get(self, request, pk, format=None):
            Uzytkownik = self.get_object(pk)
            serializer = UzytkownikSerializer(Uzytkownik)
            return Response(serializer.data)

        def put(self, request, pk, format=None):
            Uzytkownik = self.get_object(pk)
            serializer = UzytkownikSerializer(Uzytkownik, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def delete(self, request, pk, format=None):
            Uzytkownik = self.get_object(pk)
            Uzytkownik.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


        #permission_classes = [IsAdminUser]




class Opcje_BiletuTworzy(generics.ListCreateAPIView, mixins.ListModelMixin):
    queryset = Opcje_Biletu.objects.all()
    serializer_class = Opcje_BiletuSerializer

    def get(self, request):
        return self.list(request)



class Opcje_BiletuList(APIView):

    def get(self, request, format=None):
        Opcje_Biletow = Opcje_Biletu.objects.all()
        serializer = UzytkownikSerializer(Opcje_Biletow, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer =Opcje_BiletuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'status': 'Zaloguj się jako Użytkownik'
        }
        return Response(content)





class Opcje_BiletuDetale(APIView):

        def get_object(self, pk):
            try:
                return Opcje_Biletu.objects.get(pk=pk)
            except Opcje_Biletu.DoesNotExist:
                raise Http404

        def get(self, request, pk, format=None):
            Opcje_Biletu = self.get_object(pk)
            serializer = Opcje_BiletuSerializer(Opcje_Biletu)
            return Response(serializer.data)

        def put(self, request, pk, format=None):
            Opcje_Biletu = self.get_object(pk)
            serializer = Opcje_BiletuSerializer(Opcje_Biletu, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def delete(self, request, pk, format=None):
            Opcje_Biletu = self.get_object(pk)
            Opcje_Biletu.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


        permission_classes = [IsAdminUser]

        def get(self, request, format=None):
            content = {
                'status': 'Zaloguj się jako Admin'
        }
            return Response(content)




class PodrozeTworzy(generics.ListCreateAPIView, mixins.ListModelMixin):
    queryset = Podroze.objects.all()
    serializer_class = PodrozeSerializer

    def get(self, request):
        return self.list(request)




class PodrozeList(APIView):

    def get(self, request, format=None):
        Podrozee = Podroze.objects.all()
        serializer = PodrozeSerializer(Podrozee, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PodrozeSerializer(data=request.data)
        if serializer.is_valid():
                serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'status': 'Zaloguj się jako Użytkownik'
        }
        return Response(content)





class PodrozeDetale(APIView):

    def get_object(self, pk):
        try:
            return Podroze.objects.get(pk=pk)
        except Podroze.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Podroze = self.get_object(pk)
        serializer = PodrozeSerializer(Podroze)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Podroze = self.get_object(pk)
        serializer = PodrozeSerializer(Podroze, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Podroze = self.get_object(pk)
        Podroze.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    permission_classes = [IsAdminUser]

    def get(self, request, format=None):
        content = {
            'status': 'Zaloguj się jako Admin'
        }
        return Response(content)




class PociagTworzy(generics.ListCreateAPIView, mixins.ListModelMixin):
    queryset = Pociag.objects.all()
    serializer_class = PociagSerializer

    def get(self, request):
        return self.list(request)

class PociagList(APIView):

    def get(self, request, format=None):
        Pociagi = Pociag.objects.all()
        serializer = PociagSerializer(Pociagi, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PociagSerializer(data=request.data)
        if serializer.is_valid():
                serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'status': 'Zaloguj się jako Użytkownik'
        }
        return Response(content)





class PociagDetale(APIView):

    def get_object(self, pk):
        try:
            return Pociag.objects.get(pk=pk)
        except Pociag.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Pociag = self.get_object(pk)
        serializer = PociagSerializer(Podroze)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Pociag = self.get_object(pk)
        serializer = PociagSerializer(Podroze, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Pociag = self.get_object(pk)
        Pociag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    permission_classes = [IsAdminUser]

    def get(self, request, format=None):
        content = {
            'status': 'Zaloguj się jako Admin'
        }
        return Response(content)




class WagonTworzy(generics.ListCreateAPIView, mixins.ListModelMixin):
    queryset = Wagon.objects.all()
    serializer_class = WagonSerializer

    def get(self, request):
        return self.list(request)



class WagonList(APIView):

    def get(self, request, format=None):
        Wagony = Wagon.objects.all()
        serializer = WagonSerializer(Wagony, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WagonSerializer(data=request.data)
        if serializer.is_valid():
                serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'status': 'Zaloguj się jako Użytkownik'
        }
        return Response(content)





class WagonDetale(APIView):

    def get_object(self, pk):
        try:
            return Wagon.objects.get(pk=pk)
        except Wagon.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):
        Wagon = self.get_object(pk)
        serializer = WagonSerializer(wagon)
        return Response(serializer.data)


    def put(self, request, pk, format=None):
        Wagon = self.get_object(pk)
        serializer = WagonSerializer(Wagon, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        Wagon = self.get_object(pk)
        Wagon.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    permission_classes = [IsAdminUser]

    def get(self, request, format=None):
        content = {
            'status': 'Zaloguj się jako Admin'
        }
        return Response(content)


class MiejsceTworzy(generics.ListCreateAPIView, mixins.ListModelMixin):
    queryset = Miejsce.objects.all()
    serializer_class = MiejsceSerializer

    def get(self, request):
        return self.list(request)



class MiejsceList(APIView):

    def get(self, request, format=None):
        Miejsca = Miejsce.objects.all()
        serializer = MiejsceSerializer(Miejsca, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MiejsceSerializer(data=request.data)
        if serializer.is_valid():
                serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'status': 'Zaloguj się jako Użytkownik'
        }
        return Response(content)



class MiejsceDetale(APIView):

    def get_object(self, pk):
        try:
            return Miejsce.objects.get(pk=pk)
        except Miejsce.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Miejsce = self.get_object(pk)
        serializer = MiejsceSerializer(Miejsce)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Miejsce = self.get_object(pk)
        serializer = MiejsceSerializer(Miejsce, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Miejsce = self.get_object(pk)
        Miejsce.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    permission_classes = [IsAdminUser]

    def get(self, request, format=None):
        content = {
            'status': 'Zaloguj się jako Admin'
        }
        return Response(content)



class BiletTworzy(generics.ListCreateAPIView, mixins.ListModelMixin):
    queryset = Bilet.objects.all()
    serializer_class = BiletSerializer

    def get(self, request):
        return self.list(request)


class BiletList(APIView):

    def get(self, request, format=None):
        Bilety = Bilet.objects.all()
        serializer = BiletSerializer(Bilety, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BiletSerializer(data=request.data)
        if serializer.is_valid():
                serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'status': 'Zaloguj się jako Użytkownik'
        }
        return Response(content)




class BiletyDetale(APIView):

    def get_object(self, pk):
        try:
            return Bilet.objects.get(pk=pk)
        except Bilet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Bilet = self.get_object(pk)
        serializer = BiletSerializer(Bilet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Bilet = self.get_object(pk)
        serializer = BiletSerializer(Bilet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Bilet = self.get_object(pk)
        Bilet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    permission_classes = [IsAdminUser]

    def get(self, request, format=None):
        content = {
            'status': 'Zaloguj się jako Admin'
        }
        return Response(content)

