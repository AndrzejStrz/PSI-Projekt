from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.reverse import reverse

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'

class Ticket_OptionsList(generics.ListCreateAPIView):
    queryset = Ticket_Options.objects.all()
    serializer_class = Ticket_OptionsSerializer
    name = 'ticket_options-list'

class Ticket_OptionsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket_Options.objects.all()
    serializer_class = Ticket_OptionsSerializer
    name = 'ticket_options-detail'

class TravelList(generics.ListCreateAPIView):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer
    name = 'travel-list'

class TravelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer
    name = 'travel-detail'

class TrainList(generics.ListCreateAPIView):
    queryset = Train.objects.all()
    serializer_class = TrainSerializer
    name = 'train-list'

class TrainDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Train.objects.all()
    serializer_class = TrainSerializer
    name = 'train-detail'

class CarriageList(generics.ListCreateAPIView):
    queryset = Carriage.objects.all()
    serializer_class = CarriageSerializer
    name = 'carriage-list'

class CarriageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Carriage.objects.all()
    serializer_class = CarriageSerializer
    name = 'carriage-detail'

class SeatsList(generics.ListCreateAPIView):
    queryset = Seats.objects.all()
    serializer_class = SeatsSerializer
    name = 'seats-list'

class SeatsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Seats.objects.all()
    serializer_class = SeatsSerializer
    name = 'seats-detail'

class TicketList(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    name = 'ticket-list'

class TicketDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    name = 'ticket-detail'

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request):
        return Response({'User': reverse(UserList.name, request=request),
                         'Ticket_Options': reverse(Ticket_OptionsList.name, request=request),
                         'Travel': reverse(TravelList.name, request=request),
                         'Train': reverse(TrainList.name, request=request),
                         'Carriage': reverse(CarriageList.name, request=request),
                         'Seats': reverse(SeatsList.name, request=request),
                         'Ticket': reverse(TicketList.name, request=request),

                         })
