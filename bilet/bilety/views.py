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
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet
from rest_framework.reverse import reverse


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'User-list'


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'User-detail'


class Ticket_OptionsList(generics.ListCreateAPIView):
    queryset = Ticket_Options.objects.all()
    serializer_class = Ticket_OptionsSerializer
    name = 'Ticket_Options-list'


class Ticket_OptionsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket_Options.objects.all()
    serializer_class = Ticket_OptionsSerializer
    name = 'Ticket_Options-detail'


class TravelList(generics.ListCreateAPIView):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer
    name = 'Travel-list'


class TravelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer
    name = 'Travel-detail'


class TrainList(generics.ListCreateAPIView):
    queryset = Train.objects.all()
    serializer_class = TrainSerializer
    name = 'Train-list'


class TrainDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Train.objects.all()
    serializer_class = TrainSerializer
    name = 'Train-detail'


class CarriageList(generics.ListCreateAPIView):
    queryset = Carriage.objects.all()
    serializer_class = CarriageSerializer
    name = 'Carriage-list'


class CarriageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Carriage.objects.all()
    serializer_class = CarriageSerializer
    name = 'Carriage-detail'


class SeatsList(generics.ListCreateAPIView):
    queryset = Seats.objects.all()
    serializer_class = SeatsSerializer
    name = 'Seats-list'


class SeatsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Seats.objects.all()
    serializer_class = SeatsSerializer
    name = 'Seats-detail'


class TicketList(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    name = 'Ticket-list'

class TicketDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    name = 'Ticket-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({'User': reverse(UserList.name, request=request),
                         'Ticket_Options': reverse(Ticket_OptionsList.name, request=request),
                         'Travel': reverse(TravelList.name, request=request),
                         'Train': reverse(TrainList.name, request=request),
                         'Carriage': reverse(CarriageList.name, request=request),
                         'Seats': reverse(SeatsList.name, request=request),
                         'Ticket': reverse(TicketList.name, request=request),

                         })