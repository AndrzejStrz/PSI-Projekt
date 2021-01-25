from rest_framework import serializers

from .views import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    Tickets = serializers.HyperlinkedIdentityField(many=True, read_only=True, view_name='ticket-detail')

    class Meta:
        model = User
        fields = ['pk', 'url', 'Name', 'Surname', 'Login', 'Password', 'Mail', 'Tickets']

class Ticket_OptionsSerializer(serializers.HyperlinkedModelSerializer):
    Ticket_Options_Ticket = serializers.HyperlinkedIdentityField(many=True, read_only=True, view_name='ticket-detail')

    class Meta:
        model = Ticket_Options
        fields = ['Price', 'Ticket_Name', 'Ticket_Options_Ticket']

class TravelSerializer(serializers.HyperlinkedModelSerializer):
    Travel_Tickets = serializers.HyperlinkedIdentityField(many=True, read_only=True, view_name='ticket-detail')

    class Meta:
        model = Travel
        fields = ['Track', 'Date','Travel_Tickets']

class TrainSerializer(serializers.HyperlinkedModelSerializer):
    Carriages = serializers.HyperlinkedIdentityField(many=True, read_only=True, view_name='carriage-detail')
    Train_Tickets = serializers.HyperlinkedIdentityField(many=True, read_only=True, view_name='ticket-detail')

    class Meta:
        model = Train
        fields = ['Name', 'Carriages', 'Train_Tickets']


class CarriageSerializer(serializers.HyperlinkedModelSerializer):
    Seats = serializers.HyperlinkedIdentityField(many=True, read_only=True, view_name='seats-detail')

    class Meta:
        model = Carriage
        fields = ['Number_Of_Seats', 'Train_Carriage', 'Seats']


class SeatsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seats
        fields = ['Seats_Number', 'Ticket_Number', 'Carriage_Seats']


class TicketSerializer(serializers.HyperlinkedModelSerializer):
    Train_Ticket = serializers.SlugRelatedField(queryset=Train.objects.all(), slug_field='Name')
    Ticket_Options_Ticket = serializers.SlugRelatedField(queryset=Ticket_Options.objects.all(), slug_field='Ticket_Name')
    Travels_Ticket = serializers.SlugRelatedField(queryset=Travel.objects.all(), slug_field='Track')
    Ticket_User = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='Surname')

    class Meta:
        model = Ticket
        fields = ['Train_Ticket', 'Ticket_Options_Ticket', 'Travels_Ticket', 'Ticket_User']
