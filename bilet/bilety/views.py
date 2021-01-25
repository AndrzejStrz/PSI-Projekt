from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework import permissions

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'
    permission_classes = [permissions.IsAuthenticated]

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'
    permission_classes = [permissions.IsAuthenticated]

class Ticket_OptionsList(generics.ListCreateAPIView):
    queryset = Ticket_Options.objects.all()
    serializer_class = Ticket_OptionsSerializer
    name = 'ticket_options-list'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class Ticket_OptionsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket_Options.objects.all()
    serializer_class = Ticket_OptionsSerializer
    name = 'ticket_options-detail'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class TravelList(generics.ListCreateAPIView):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer
    name = 'travel-list'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class TravelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer
    name = 'travel-detail'
    permission_classes = [permissions.IsAuthenticated]

class TrainList(generics.ListCreateAPIView):
    queryset = Train.objects.all()
    serializer_class = TrainSerializer
    name = 'train-list'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class TrainDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Train.objects.all()
    serializer_class = TrainSerializer
    name = 'train-detail'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CarriageList(generics.ListCreateAPIView):
    queryset = Carriage.objects.all()
    serializer_class = CarriageSerializer
    name = 'carriage-list'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CarriageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Carriage.objects.all()
    serializer_class = CarriageSerializer
    name = 'carriage-detail'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SeatsList(generics.ListCreateAPIView):
    queryset = Seats.objects.all()
    serializer_class = SeatsSerializer
    name = 'seats-list'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SeatsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Seats.objects.all()
    serializer_class = SeatsSerializer
    name = 'seats-detail'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class TicketList(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    name = 'ticket-list'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class TicketDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    name = 'ticket-detail'
    permission_classes = [permissions.IsAuthenticated]

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
