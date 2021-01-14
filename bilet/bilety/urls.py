
from django.urls import path
from . import views
from rest_framework import generics


urlpatterns = [
    #path('', views.index, name='index'),



    path('User', views.UserList.as_view(), name=views.UserList.name),
    path('User/<int:pk>', views.UserDetail.as_view(), name=views.UserDetail.name),

    path('Opcje_Biletu', views.Ticket_OptionsList.as_view(), name=views.Ticket_OptionsList.name),
    path('Opcje_Biletu/<int:pk>', views.Ticket_OptionsDetail.as_view(), name=views.Ticket_OptionsDetail.name),

    path('Podroze', views.TravelList.as_view(), name=views.TravelList.name),
    path('Podroze/<int:pk>', views.TravelDetail.as_view(), name=views.TravelDetail.name),

    path('Pociag', views.TrainList.as_view(), name=views.TrainList.name),
    path('Pociag/<int:pk>', views.TrainDetail.as_view(), name=views.TrainDetail.name),

    path('Wagon', views.CarriageList.as_view(), name=views.CarriageList.name),
    path('Wagon/<int:pk>', views.CarriageDetail.as_view(), name=views.CarriageDetail.name),

    path('Miejsce', views.SeatsList.as_view(), name=views.SeatsList.name),
    path('Miejsce/<int:pk>', views.SeatsDetail.as_view(), name=views.SeatsDetail.name),

    path('Bilet', views.TicketList.as_view(), name=views.TicketList.name),
    path('Bilet/<int:pk>', views.TicketDetail.as_view(), name=views.TicketDetail.name),

    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),



]
